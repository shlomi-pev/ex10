from vector import Vector
from math import radians, sqrt
from copy import copy

class SpaceObject:

    def __init__(self, location=None, velocity=None, heading=0.0, radios=1):
        self.location = location if location else Vector()
        self.velocity = velocity if velocity else Vector()
        self.heading = heading
        self.radios = radios

    def get_location(self):
        return self.location.get_as_tuple()

    def has_intersection(self, obj):
        obj_x, obj_y = obj.get_location()
        my_x, my_y = self.get_location()
        distance = sqrt((obj_x - my_x) ** 2 + (obj_y - my_y) ** 2)
        return distance <= self.radios + obj.radios

    def get_heading_rad(self):
        return radians(self.heading)

    def get_heading(self):
        return self.heading

    def get_velocity(self):
        return self.velocity.get_as_tuple()

    def move(self, min_v: Vector, max_v: Vector):
        delta_x = max_v.get_x() - min_v.get_x()
        delta_y = max_v.get_y() - min_v.get_y()
        new_x = min_v.get_x() + \
                (self.location.get_x() + self.velocity.get_x() -
                 min_v.get_x()) % delta_x
        new_y = min_v.get_y() + \
                (self.location.get_y() + self.velocity.get_y() -
                 min_v.get_y()) % delta_y
        self.location = Vector(new_x, new_y)

    def __copy__(self):
        return SpaceObject(copy(self.location), copy(self.velocity),
                           self.heading)

