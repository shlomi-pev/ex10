from vector import Vector
from math import radians, sqrt
from copy import copy


class SpaceObject:
    """
    this class is the basic representation of an object floating in 2D space
    """
    def __init__(self, location=None, velocity=None, heading=0.0, radios=0):
        """

        :param location: Vector representing the object location
        :param velocity: Vector representing the object location
        :param heading: heading in degrees
        :param radios: radios in int
        """
        self.location = location if location else Vector()
        self.velocity = velocity if velocity else Vector()
        self.heading = heading
        self.radios = radios

    def get_location(self):
        """
        :return: the location in the form (x,y)
        """
        return self.location.get_as_tuple()

    def has_intersection(self, obj):
        """
        this function check if to space object are close enough to collide
        :param obj: the other object
        :return: true if collided else false
        """
        obj_x, obj_y = obj.get_location()
        my_x, my_y = self.get_location()
        #  calculating the distance
        distance = sqrt((obj_x - my_x) ** 2 + (obj_y - my_y) ** 2)
        return distance <= self.radios + obj.radios

    def get_heading_rad(self):
        """
        :return: heading converted to radians
        """
        return radians(self.heading)

    def get_heading(self):
        """
        :return: heading in degrees
        """
        return self.heading

    def get_velocity(self):
        """
        :return: a tuple in the form (speed_in_x, speed_in_y)
        """
        return self.velocity.get_as_tuple()

    def move(self, min_v, max_v):
        """
        this function calculates and updates a new location according to the
         boundaries of the screen and the objects velocity
        :param min_v: a Vector representing the lower left corner of the
        screen
        :param max_v: a Vector representing the upper right corner of the
        screen
        :return:
        """
        delta_x = max_v.get_x() - min_v.get_x()
        delta_y = max_v.get_y() - min_v.get_y()
        #  calculates new location in x axis
        new_x = min_v.get_x() + \
                (self.location.get_x() + self.velocity.get_x() -
                 min_v.get_x()) % delta_x
        #  calculates new location in y axis
        new_y = min_v.get_y() + \
                (self.location.get_y() + self.velocity.get_y() -
                 min_v.get_y()) % delta_y
        self.location = Vector(new_x, new_y)

    def __copy__(self):
        """
        :return: a copy of the instance
        """
        return SpaceObject(copy(self.location), copy(self.velocity),
                           self.heading)

