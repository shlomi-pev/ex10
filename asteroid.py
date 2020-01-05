from space_object import SpaceObject
from vector import Vector


class Asteroid(SpaceObject):
    def __init__(self, location, velocity, size=3):
        heading = 0.0
        radios = size*10 - 5
        SpaceObject.__init__(self, location, velocity, heading, radios)
        self.__size = size