from random import uniform


class Vector:
    """
    a vector in 2D space
    """
    def __init__(self, x_val=0.0, y_val=0.0):
        """
        creates a new instance of class Vector
        :param x_val: the val in the X axis
        :param y_val: the val in the Y axis
        """
        self._x = x_val
        self._y = y_val

    def get_x(self):
        """
        :return: the val in the X axis
        """
        return self._x

    def get_y(self):
        """
        :return: the val in the Y axis
        """
        return self._y

    def get_as_tuple(self):
        """
        :return: a tuple in the form (x, y)
        """
        return self._x, self._y

    def __copy__(self):
        """
        :return: a copy of the current instance
        """
        return Vector(self._x, self._y)

    @classmethod
    def random(cls, min_v, max_v):
        """
        generates a new Vector with value between min and max.
        :param min_v: the vector representing the minimum value in every axis
        :param max_v: the vector representing the maximum value in every axis
        :return: a new random vector
        """
        x = uniform(min_v.get_x(), max_v.get_x())
        y = uniform(min_v.get_y(), max_v.get_y())
        return Vector(x, y)
