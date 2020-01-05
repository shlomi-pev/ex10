from vector import Vector
from math import radians, sqrt


class SpaceObject:

    def __init__(self, location=None, velocity=None, heading=0.0, radios=1):
        self._location = location if location else Vector()
        self._velocity = velocity if velocity else Vector()
        self._heading = heading
        self._radios = radios

    def get_location(self):
        return self._location.get_as_tuple()

    def has_intersection(self, obj):
        obj_x, obj_y = obj.get_location()
        my_x, my_y = self.get_location()
        distance = sqrt((obj_x - my_x) ** 2 + (obj_y - my_y) ** 2)
        return distance <= self._radios + obj._radios

    def get_heading_rad(self):
        return radians(self._heading)

    def move(self, min_v: Vector, max_v: Vector):
        delta_x = max_v.get_x() - min_v.get_x()
        delta_y = max_v.get_y() - min_v.get_y()
        new_x = min_v.get_x() + \
                (self._location.get_x() + self._velocity.get_x() -
                 min_v.get_x()) % delta_x
        new_y = min_v.get_y() + \
                (self._location.get_y() + self._velocity.get_y() -
                 min_v.get_y()) % delta_y
        self._location = Vector(new_x, new_y)
