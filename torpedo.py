from space_object import SpaceObject
from vector import Vector, Direction_Vector


class Torpedo(SpaceObject):
    def __init__(self, location=None, velocity=None, orientation=None):
        SpaceObject.__init__(self, location, velocity, orientation)