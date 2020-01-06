from space_object import SpaceObject
from vector import Vector
from copy import copy
from math import sin, cos, radians
RADIOS = 4

class Torpedo(SpaceObject):
    def __init__(self, ship, time_of_creation):
        """
        initiating a new instance of class Torpedo
        :param ship: the ship that shot the torpedo
        :param time_of_creation: the time the torpedo was created in
        relation to the game
        """

        location = copy(ship.location)
        heading = ship.heading
        velocity = self.__calc_torpedo_velocity(ship.velocity, radians(heading))
        SpaceObject.__init__(self, location, velocity, heading, RADIOS)
        self.__time_of_creation = time_of_creation

    def get_time_of_creation(self):
        """
        :return: the time (in relation to the game) in which the torpedo was
        created
        """
        return self.__time_of_creation

    def __calc_torpedo_velocity(self, velocity:Vector, heading):
        """
        calculates the velocity according to the velocity and heading of
        the shit that shot it
        :param velocity: the velocity of the shooting ship
        :param heading:
        :return:
        """
        #  calculates the new value in every axis
        new_x = velocity.get_x()+2 * cos(heading)
        new_y = velocity.get_y()+2 * sin(heading)
        #  generates new velocity vector
        return Vector(new_x, new_y)


