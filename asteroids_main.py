from screen import Screen
import sys
from ship import *
from asteroid import *
from torpedo import *
from vector import *
import random as r

DEFAULT_ASTEROIDS_NUM = 5
TURN_RIGHT = -7
TURN_LEFT = 7
TORPEDO_LIMIT = 10
TORPEDO_LIFE = 200
SCORES = {3: 20, 2: 50, 1: 100}


class GameRunner:

    def __init__(self, asteroids_amount):
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
        self.__ship.random_teleport(self.__screen_min, self.__screen_max)
        self.__astroids_list = self.__generate_asteroids(asteroids_amount)
        self.__torpedos_list = list()
        self.__game_length = 0

    def gen_ship(self):
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
        for asteroid in self.__astroids_list:
            if asteroid.has_intersection(self.__ship):
                self.__screen.show_message("COLLISION",
                                           "be careful, watch out from asteroids")
                self.__screen.unregister_asteroid(asteroid)
                self.__astroids_list.remove(asteroid)
                self.__ship_life -= 1
                if self.__ship_life > 0:
                    self.__screen.remove_life()


    def __check_if_end(self):
        end = False
        if len(self.__astroids_list) == 0:
            self.__screen.show_message("you won",
                                       "great job")
            end = True
        if self.__ship_life <= 0:
            self.__screen.show_message("no life left",
                                       "the game is over loser")
            end = True
        if self.__screen.should_end():
            self.__screen.show_message("oh no",
                                      "please don't go")
            end = True
        if end:
            self.__screen.end_game()
            sys.exit()


    def _game_loop(self):
        self.__check_if_end()
        self.__game_length += 1
        #  check for collision destroys asteroid if necessary and removes a
        #  life \ ends the game if needed
        self.__ship_collision()
        #  checks for torpedo and asteroids collision, destroys and splits
        #  the asteroid if necessary
        self.__torpedo_collision()
        self.__remove_old_torpedos(self.__game_length)

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
        rand = lambda: r.choice((-1, 1)) * r.uniform(1, 4)
        size = 3
        asteroids_list = list()
        for i in range(asteroids_amount):
            velocity = Vector(rand(), rand())
            location = Vector.random(self.__screen_min, self.__screen_max)
            new_asteroid = Asteroid(location, velocity, size)
            while new_asteroid.has_intersection(self.__ship):
                location = Vector.random(self.__screen_min, self.__screen_max)
                new_asteroid = Asteroid(location, velocity, size)
            asteroids_list.append(new_asteroid)
            self.__screen.register_asteroid(new_asteroid, size)
        return asteroids_list

    def draw_all(self):
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
        #  moves the ship
        self.__ship.move(self.__screen_min, self.__screen_max)
        #  moves the asteroids
        for asteroid in self.__astroids_list:
            asteroid.move(self.__screen_min, self.__screen_max)
        #  moves the torpedos
        for torpedo in self.__torpedos_list:
            torpedo.move(self.__screen_min, self.__screen_max)

    def __destroy_asteroid(self, asteroid, torpedo):
        self.__torpedos_list.remove(torpedo)
        self.__astroids_list.remove(asteroid)
        self.__screen.unregister_torpedo(torpedo)
        self.__screen.unregister_asteroid(asteroid)
        old_size = asteroid.get_size()
        if old_size > 1:
            new_asteroid1, new_asteroid2 = asteroid.split(torpedo)
            self.__screen.register_asteroid(new_asteroid1, old_size)
            self.__screen.register_asteroid(new_asteroid2, old_size)
            self.__astroids_list.extend((new_asteroid1, new_asteroid2))

    def __torpedo_collision(self):
        for torpedo in self.__torpedos_list:
            for asteroid in self.__astroids_list:
                if asteroid.has_intersection(torpedo):
                    self.__player_score += SCORES[asteroid.get_size()]
                    self.__screen.set_score(self.__player_score)
                    self.__destroy_asteroid(asteroid, torpedo)

    def __shoot_torpedo(self, time_of_creation):
        if len(self.__torpedos_list) == TORPEDO_LIMIT:
            return
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
