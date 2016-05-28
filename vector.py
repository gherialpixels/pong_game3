import cmath

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        '''
        Returns the dot (inner) product of two vectors
        :param other: the other vector
        :return: a scalar
        '''
        return self.x * other.x + self.y * other.y

    def norm2(self):
        return cmath.sqrt(self.x ** 2 + self.y ** 2)

ZERO = Vector(0, 0)
UP = Vector(0, 1)
RIGHT = Vector(1, 0)