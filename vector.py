import math as m
import random as r

class Vector:
    def __init__(self, x_val=0.0, y_val=0.0):
        self.x = x_val
        self.y = y_val

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x_val):
        self.x = float(x_val)

    def set_y(self, y_val):
        self.y = float(y_val)

    @classmethod
    def random(cls, min_v, max_v):
        x = r.randint(min_v.get_x(), max_v.get_x())
        y = r.randint(min_v.get_y(), max_v.get_y())
        return Vector(x, y)


class Direction_Vector(Vector):
    def __init__(self):
        Vector.__init__(self, 1.0, 0.0)

    def rotate(self, deg):
        """
        rotates the vector by the given degrees
        :param deg: value in degrees
        :return:
        """
        rad = m.radians(deg)
        # px = x * cs - y * sn;
        # py = x * sn + y * cs;
        cs = m.cos(rad)
        sn = m.sin(rad)
        new_x = self.x*cs - self.y*sn
        new_y = self.x*sn - self.y*cs
        self.x = new_x
        self.y = new_y

    def get_angel_deg(self):
        if self.x == 0:
            return 90 if self.y > 0 else 270
        else:
            return m.degrees(m.tan(self.y/self.x))
