from space_object import SpaceObject
from vector import Vector, Direction_Vector


class Ship(SpaceObject):
    def __init__(self, location=None, velocity=None, orientation=None):
        SpaceObject.__init__(self, location, velocity, orientation)

    def random_teleport(self, min_v, max_v):
        self._location = Vector.random(min_v, max_v)

    def get_heading(self):
        return self._orientation.get_angel_deg()

    def rotate(self, angle):
        self._orientation.rotate(angle)
