# -*- coding: utf-8 -*-


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    __repr__ = __str__

    @property
    def neighbors(self):
        return (self.left, self.right, self.up, self.down)

    @property
    def left(self):
        return Point(self.x - 1, self.y)

    @property
    def right(self):
        return Point(self.x + 1, self.y)

    @property
    def up(self):
        return Point(self.x, self.y - 1)

    @property
    def down(self):
        return Point(self.x, self.y + 1)

    def __getitem__(self, index):
        if isinstance(index, int):
            return (self.x, self.y)[index]
        return getattr(self, index)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])
