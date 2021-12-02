#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT = '523764819'
TEST = '389125467'


class Circle:

    def __init__(self, labels):
        self.labels = list(map(int, labels))
        self._len = len(labels)
        self._max = max(self.labels)
        self.pos = 0

    @property
    def label(self):
        return self.labels[self.pos % self._len]


def main():
    circle = Circle(TEST)
    # circle = list(map(int, TEST))


if __name__ == '__main__':
    main()
