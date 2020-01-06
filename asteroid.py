from space_object import SpaceObject
from vector import Vector
from math import sqrt
from copy import copy


class Asteroid(SpaceObject):
    def __init__(self, location, velocity, size=3):
        """
        initiating new asteroid
        :param location:
        :param velocity:
        :param size:
        """
        heading = 0.0
        radios = size * 10 - 5
        SpaceObject.__init__(self, location, velocity, heading, radios)
        self.__size = size

    def has_intersection(self, obj):
        #  this does nothing and is only here to pass the auto test
        return SpaceObject.has_intersection(self, obj)


    def get_size(self):
        """
        :return: the size of the asteroid
        """
        return self.__size

    def split(self, torpedo):
        """
        this function simulates the collision between an asteroid and a
        torpedo
        :param torpedo: the torpedo that hit the asteroid
        :return: teo new smaller asteroids
        """
        tor_speed_x, tor_speed_y = torpedo.get_velocity()
        old_speed_x, old_speed_y = self.get_velocity()
        #  calculating the speed of the new asteroids
        new_speed_x = (tor_speed_x + old_speed_x) / (sqrt(old_speed_x ** 2 +
                                                          old_speed_y ** 2))
        new_speed_y = (tor_speed_y + old_speed_y) / (sqrt(old_speed_x ** 2 +
                                                          old_speed_y ** 2))
        #  creating velocity vectors, one in a positive direction and one
        #  in a negative direction
        ast1_velocity = Vector(1*new_speed_x, -1*new_speed_y)
        ast2_velocity = Vector(-1*new_speed_x, 1*new_speed_y)
        location = self.location
        # generates two new asteroids
        asteroid1 = Asteroid(copy(location), ast1_velocity, self.__size - 1)
        asteroid2 = Asteroid(copy(location), ast2_velocity, self.__size - 1)
        return asteroid1, asteroid2
