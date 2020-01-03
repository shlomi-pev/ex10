import math as m


class Vector:
    def __init__(self, x_val=0.0, y_val=0.0):
        self.__x = x_val
        self.__y = y_val

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x_val):
        self.__x = float(x_val)

    def set_y(self, y_val):
        self.__y = float(y_val)


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
        new_x = self.__x*cs - self.__y*sn
        new_y = self.__x*sn - self.__y*cs
        self.__x = new_x
        self.__y = new_y
