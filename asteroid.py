from space_object import SpaceObject
from vector import Vector


class Asteroid(SpaceObject):
    def __init__(self, location, velocity, size=3):
        SpaceObject.__init__(self, location, velocity, 0.0)
        self.__size = size