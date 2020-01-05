from space_object import SpaceObject
from vector import Vector
from math import sin,cos

class Ship(SpaceObject):
    def __init__(self, location=None, velocity=None, heading=0.0):
        SpaceObject.__init__(self, location, velocity, heading)

    def random_teleport(self, min_v, max_v):
        self._location = Vector.random(min_v, max_v)

    def get_heading(self):
        return self._heading

    def rotate(self, angle):
        self._heading += angle

    def accelerate(self):
        new_x = self._velocity.get_x() + cos(self.get_heading_rad())
        new_y = self._velocity.get_y() + sin(self.get_heading_rad())
        self._velocity = Vector(new_x, new_y)
