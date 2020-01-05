from space_object import SpaceObject
from vector import Vector, Direction_Vector


class Torpedo(SpaceObject):
    def __init__(self, location, velocity, orientation):
        SpaceObject.__init__(self, location, velocity, orientation)