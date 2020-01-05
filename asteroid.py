from space_object import SpaceObject
from vector import Vector
from math import sqrt
from copy import copy


class Asteroid(SpaceObject):
    def __init__(self, location, velocity, size=3):
        heading = 0.0
        radios = size * 10 - 5
        SpaceObject.__init__(self, location, velocity, heading, radios)
        self.__size = size

    def get_size(self):
        return self.__size

    def split(self, torpedo):
        tor_speed_x, tor_speed_y = torpedo.get_velocity()
        old_speed_x, old_speed_y = self.get_velocity()
        new_speed_x = (tor_speed_x + old_speed_x) / (sqrt(old_speed_x ** 2 +
                                                          old_speed_y ** 2))
        new_speed_y = (tor_speed_y + old_speed_y) / (sqrt(old_speed_x ** 2 +
                                                          old_speed_y ** 2))
        ast1_velocity = Vector(new_speed_x, new_speed_y)
        ast2_velocity = Vector(-new_speed_x, -new_speed_y)
        location = self.location
        asteroid1 = Asteroid(copy(location), ast1_velocity, self.__size - 1)
        asteroid2 = Asteroid(copy(location), ast2_velocity, self.__size - 1)
        return asteroid1, asteroid2
