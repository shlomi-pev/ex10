from screen import Screen
import sys
from ship import *
from asteroid import *
from torpedo import *
from vector import *
DEFAULT_ASTEROIDS_NUM = 5
TURN_RIGHT = -7
TURN_LEFT = 7

class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__screen_min = Vector(self.__screen_min_x,self.__screen_min_y)
        self.__screen_max = Vector(self.__screen_max_x, self.__screen_max_y)
        # generating ship and placing on screen
        self.__ship = Ship()
        self.__ship.random_teleport(self.__screen_min, self.__screen_max)
        ship_x ,ship_y = self.__ship.get_location()
        ship_h = self.__ship.get_heading()
        self.__screen.draw_ship(ship_x, ship_y, ship_h)


    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!

        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        if self.__screen.is_right_pressed():
            self.__ship.rotate(TURN_RIGHT)
        if self.__screen.is_left_pressed():
            self.__ship.rotate(TURN_LEFT)
        if self.__screen.is_up_pressed():
            self.__ship.accelerate()

        self.__ship.move(self.__screen_min,self.__screen_max)

        self.__screen.draw_ship(self.__ship.get_location()[0],
                                self.__ship.get_location()[1],
                                self.__ship.get_heading())


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
