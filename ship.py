from space_object import SpaceObject
from vector import Vector
from math import sin, cos
RADIOS = 1
class Ship(SpaceObject):
    def __init__(self, location=None, velocity=None, heading=0.0):
        SpaceObject.__init__(self, location, velocity, heading, RADIOS)

    def random_teleport(self, min_v, max_v):
        self.location = Vector.random(min_v, max_v)

    def rotate(self, angle):
        self.heading += angle

    def accelerate(self):
        new_x = self.velocity.get_x() + cos(self.get_heading_rad())
        new_y = self.velocity.get_y() + sin(self.get_heading_rad())
        self.velocity = Vector(new_x, new_y)
