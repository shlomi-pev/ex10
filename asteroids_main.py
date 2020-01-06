from screen import Screen
import sys
from ship import *
from asteroid import *
from torpedo import *
from vector import *
import random as r
# sets all magic numbers and defaults
DEFAULT_ASTEROIDS_NUM = 5
TURN_RIGHT = -7
TURN_LEFT = 7
TORPEDO_LIMIT = 10
TORPEDO_LIFE = 200
SCORES = {3: 20, 2: 50, 1: 100}
DEFAULT_ASTEROIDS_SIZE = 3
MIN_ASTEROID_SIZE = 1


class GameRunner:
    """
    this is a class that runs the most confusing game known to men
    """
    def __init__(self, asteroids_amount):
        """
        creates a new game with the given amount if asteroids
        :param asteroids_amount:
        """
        self.__screen = Screen()
        self.__player_score = 0
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__screen_min = Vector(self.__screen_min_x, self.__screen_min_y)
        self.__screen_max = Vector(self.__screen_max_x, self.__screen_max_y)
        # generating ship and placing on screen
        self.__ship = self.gen_ship()
        self.__ship_life = 3
        #  creating and registering all asteroids
        self.__astroids_list = self.__generate_asteroids(asteroids_amount)
        self.__torpedos_list = list()
        self.__game_length = 0

    def gen_ship(self):
        """
        generates a ship and assign it a random location
        :return:
        """
        location = Vector.random(self.__screen_min, self.__screen_max)
        my_ship = Ship(location=location)
        return my_ship

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!

        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def __ship_collision(self):
        """
        this function checks and handles all aspects off collision between
        the ship and the asteroids
        :return:
        """
        for asteroid in self.__astroids_list:
            if asteroid.has_intersection(self.__ship):
                #  boom
                self.__screen.show_message("COLLISION",
                                           "be careful, watch out from asteroids")
                self.__screen.unregister_asteroid(asteroid)
                self.__astroids_list.remove(asteroid)
                if self.__ship_life > 0:  # makes not to remove life if ship
                    # all-ready was destroyed in  the same iteration
                    self.__ship_life -= 1
                    self.__screen.remove_life()


    def __check_if_end(self):
        """
        this function deals with the end conditions of the game
        :return:
        """
        if len(self.__astroids_list) == 0:  # player won
            self.__screen.show_message("you won",
                                       "great job")
        elif self.__ship_life <= 0:  # player lost
            self.__screen.show_message("no life left",
                                       "the game is over loser")
        elif self.__screen.should_end():  # player choose to quit
            self.__screen.show_message("oh no",
                                      "please don't go")
        else:  # no end condition is met
            return
        #  one or more end conditions is met
        #  closes the graphics and terminating the game
        self.__screen.end_game()
        sys.exit()

    def _game_loop(self):
        """
        this function runs one iteration of the gameloop
        :return:
        """
        #  checks if any end conditions are met, if so ends the game
        self.__check_if_end()
        self.__game_length += 1
        #  check for collision destroys asteroid if necessary and removes a
        #  life \ ends the game if needed
        self.__ship_collision()
        #  checks for torpedo and asteroids collision, destroys and splits
        #  the asteroid if necessary
        self.__torpedo_collision()
        self.__remove_old_torpedos(self.__game_length)

        #  next block checks for inputs from player end implements if needed
        if self.__screen.is_space_pressed():
            self.__shoot_torpedo(self.__game_length)
        if self.__screen.is_right_pressed():
            self.__ship.rotate(TURN_RIGHT)
        if self.__screen.is_left_pressed():
            self.__ship.rotate(TURN_LEFT)
        if self.__screen.is_up_pressed():
            self.__ship.accelerate()

        self.move_all()
        self.draw_all()

    def __generate_asteroids(self, asteroids_amount):
        """
        generates a list of asteroids with random location and velocity
        :param asteroids_amount: the amount of asteroids to be created
        :return: a list containing said asteroids
        """
        speed = lambda: r.choice((-1, 1)) * r.uniform(1, 4) # generates
        # random numbers so that 1<=|speed|<=4
        size = DEFAULT_ASTEROIDS_SIZE
        asteroids_list = list()
        for i in range(asteroids_amount):
            #  generates random velocity and location for the new_asteroid
            velocity = Vector(speed(), speed())
            location = Vector.random(self.__screen_min, self.__screen_max)
            # creates a new asteroid
            new_asteroid = Asteroid(location, velocity, size)
            #  checks that there are no collision between
            #  the new_asteroid and the ship
            while new_asteroid.has_intersection(self.__ship):
                location = Vector.random(self.__screen_min, self.__screen_max)
                new_asteroid = Asteroid(location, velocity, size)
            #  adds a valid asteroid to the game
            asteroids_list.append(new_asteroid)
            self.__screen.register_asteroid(new_asteroid, size)
        return asteroids_list

    def draw_all(self):
        """
        draws all the objects in the game in their correct position
        :return:
        """
        #  draws the ship
        ship_x, ship_y = self.__ship.get_location()
        ship_h = self.__ship.get_heading()
        self.__screen.draw_ship(ship_x, ship_y, ship_h)
        # draws the asteroids
        for asteroid in self.__astroids_list:
            ast_x, ast_y = asteroid.get_location()
            self.__screen.draw_asteroid(asteroid, ast_x, ast_y)
        # draws the torpedoes
        for torpedo in self.__torpedos_list:
            tor_x, tor_y = torpedo.get_location()
            tor_h = torpedo.get_heading()
            self.__screen.draw_torpedo(torpedo, tor_x, tor_y, tor_h)

    def move_all(self):
        """
        moves all the game objects to their updated location
        :return:
        """
        #  moves the ship
        self.__ship.move(self.__screen_min, self.__screen_max)
        #  moves the asteroids
        for asteroid in self.__astroids_list:
            asteroid.move(self.__screen_min, self.__screen_max)
        #  moves the torpedos
        for torpedo in self.__torpedos_list:
            torpedo.move(self.__screen_min, self.__screen_max)

    def __destroy_asteroid(self, asteroid, torpedo):
        """
        handles all aspects of a collision between an asteroid and a torpedo
        :param asteroid: an asteroid that ha collided with the given torpedo
        :param torpedo: a torpedo that has collided with the given asteroid
        :return:
        """
        #  removes both objects from the screen and lists.
        self.__torpedos_list.remove(torpedo)
        self.__screen.unregister_torpedo(torpedo)
        self.__astroids_list.remove(asteroid)
        self.__screen.unregister_asteroid(asteroid)
        old_size = asteroid.get_size()
        # checks if the asteroid is big enough to split
        if old_size > MIN_ASTEROID_SIZE:
            #  splits the big asteroid into two small ones
            new_asteroid1, new_asteroid2 = asteroid.split(torpedo)
            #  registers the two new asteroids
            self.__screen.register_asteroid(new_asteroid1, old_size)
            self.__screen.register_asteroid(new_asteroid2, old_size)
            self.__astroids_list.extend((new_asteroid1, new_asteroid2))

    def __torpedo_collision(self):
        """
        checks and handles all aspects of collision between asteroids and
        torpedoes
        :return:
        """
        for torpedo in self.__torpedos_list:
            for asteroid in self.__astroids_list:
                if asteroid.has_intersection(torpedo):
                    self.__player_score += SCORES[asteroid.get_size()]
                    self.__screen.set_score(self.__player_score)
                    self.__destroy_asteroid(asteroid, torpedo)
                    break  # handle two torpedoes hitting the same asteroid

    def __shoot_torpedo(self, time_of_creation):
        """
        handles all aspects of shooting a torpedo
        :param time_of_creation: the current time in relation to the game
        :return:
        """
        if len(self.__torpedos_list) == TORPEDO_LIMIT:
            # checks if there is space for a new torpedo
            return
        #  generates a new torpedo
        new_torpedo = Torpedo(self.__ship, time_of_creation)
        self.__torpedos_list.append(new_torpedo)
        self.__screen.register_torpedo(new_torpedo)

    def __remove_old_torpedos(self, current_time):
        for torpedo in self.__torpedos_list:
            tor_creation_time = torpedo.get_time_of_creation()
            if current_time - tor_creation_time >= TORPEDO_LIFE:
                self.__torpedos_list.remove(torpedo)
                self.__screen.unregister_torpedo(torpedo)


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
