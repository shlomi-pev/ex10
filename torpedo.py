from space_object import SpaceObject
from vector import Vector


class Torpedo(SpaceObject):
    def __init__(self, location, velocity, heading):
        SpaceObject.__init__(self, location, velocity, heading)