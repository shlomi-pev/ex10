from vector import Vector, Direction_Vector


class SpaceObject:

    def __init__(self, location=None, velocity=None, orientation=None):
        self._location = location if location else Vector()
        self._velocity = velocity if velocity else Vector()
        self._orientation = orientation if orientation else Direction_Vector()

    def get_location(self):
        return self._location.get_x(), self._location.get_y()


