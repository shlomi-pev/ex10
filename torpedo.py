from space_object import SpaceObject
from vector import Vector
from ship import Ship
from copy import copy
from math import sin, cos, radians
RADIOS = 4

class Torpedo(SpaceObject):
    def __init__(self, ship, time_of_creation):
        ship = copy(ship)
        location = ship.location
        heading = ship.heading
        velocity = self.__calc_torpedo_velocity(ship.velocity, radians(heading))
        SpaceObject.__init__(self, location, velocity, heading, RADIOS)
        self.__time_of_creation = time_of_creation

    def get_time_of_creation(self):
        return self.__time_of_creation

    def __calc_torpedo_velocity(self, velocity:Vector, heading):
        new_x = velocity.get_x()+2 * cos(heading)
        new_y = velocity.get_y()+2 * sin(heading)
        return Vector(new_x, new_y)


