from vector import Vector, Direction_Vector


class Ship:
    def __init__(self, location=None, velocity=None, orientation=None):
        self.__location = location if location else Vector()
        self.__velocity = velocity if velocity else Vector()
        self.__orientation = orientation if orientation else Direction_Vector()

    def random_teleport(self, min_v, max_v):
        self.__location = Vector.random(min_v, max_v)

    def get_heading(self):
        return self.__orientation.get_angel_deg()

    def rotate(self, angle):
        self.__orientation.rotate(angle)
