from space_object import SpaceObject
from vector import Vector


class Asteroid(SpaceObject):
    def __init__(self, location=None, velocity=None):
        SpaceObject.__init__(self, location, velocity, 0.0)