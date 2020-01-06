from space_object import SpaceObject
from vector import Vector
from math import sin, cos
RADIOS = 1  # default ship radios


class Ship(SpaceObject):
    def __init__(self, location=None, velocity=None, heading=0.0):
        """
        initiating one instance of class ship
        :param location: Vector representing ships location
        :param velocity: Vector representing ships velocity
        :param heading: heading in degrees
        """
        SpaceObject.__init__(self, location, velocity, heading, RADIOS)

    def rotate(self, theta):
        """
        rotates ships heading dy the given angle
        :param theta: an angle in degrees
        :return:
        """
        self.heading += theta

    def accelerate(self):
        """
        changes ships velocity according to its heading
        :return:
        """
        #  calculates new velocity vector using the amazing formula
        new_x = self.velocity.get_x() + cos(self.get_heading_rad())
        new_y = self.velocity.get_y() + sin(self.get_heading_rad())
        #  creates a new vector and places into the attribute velocity
        self.velocity = Vector(new_x, new_y)
