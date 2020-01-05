import math as m
import random as r

class Vector:
    def __init__(self, x_val=0.0, y_val=0.0):
        self._x = x_val
        self._y = y_val

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


    def set_x(self, x_val):
        self._x = float(x_val)

    def set_y(self, y_val):
        self._y = float(y_val)

    def get_as_tuple(self):
        return self._x, self._y

    @classmethod
    def random(cls, min_v, max_v):
        x = r.randint(min_v.get_x(), max_v.get_x())
        y = r.randint(min_v.get_y(), max_v.get_y())
        return Vector(x, y)


# class Direction_Vector(Vector):
#     def __init__(self):
#         Vector.__init__(self, 1.0, 0.0)
#
#     def rotate(self, theta):
#         """
#         rotates the vector by the given degrees
#         :param deg: value in degrees
#         :return:
#         """
#         # rad = m.radians(deg)
#         # cs = m.cos(rad)
#         # sn = m.sin(rad)
#         # new_x = self._x*cs - self._y*sn
#         # new_y = self._x*sn - self._y*cs
#         # self._x = new_x
#         # self._y = new_y
#         new_deg = theta + self.get_angel_deg()
#         self._calc_from_deg(new_deg)
#
#     def _calc_from_deg(self, theta):
#         theta = m.radians(theta)
#         self._x = m.cos(theta)
#         self._y = m.sin(theta)
#
#     def get_angel_deg(self):
#         if self._x == 0:
#             return 90 if self._y > 0 else 270
#         else:
#             return m.degrees(m.atan(self._y/self._x))
