from space_object import SpaceObject
from vector import Vector
RADIOS = 4

class Torpedo(SpaceObject):
    def __init__(self, location, velocity, heading):
        SpaceObject.__init__(self, location, velocity, heading, RADIOS)