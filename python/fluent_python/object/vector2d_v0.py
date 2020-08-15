from array import array
import path


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))



