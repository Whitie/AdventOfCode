#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT = 'input.txt'
OPEN = '.'
TREE = '#'


def read_input(filename=INPUT):
    area = []
    with open(filename) as fp:
        for line in fp:
            if line.strip():
                area.append(line.strip())
    return area


class BottomReached(Exception):
    pass


class Area:

    def __init__(self, map):
        self._map = map
        self.max_x = len(map[0])
        self.max_y = len(map)
        self.x = 0
        self.y = 0
        self.tree_count = 0
        self.step_count = 0

    @classmethod
    def from_file(cls, filename):
        area = read_input(INPUT)
        return cls(area)

    def move(self, right=3, down=1):
        self.x += right
        self.y += down
        if self.y >= self.max_y:
            raise BottomReached
        if self.x >= self.max_x:
            self.x -= self.max_x
        if self._map[self.y][self.x] == TREE:
            self.tree_count += 1
        self.step_count += 1


def main():
    area = Area.from_file(INPUT)
    while True:
        try:
            area.move()
        except BottomReached:
            break
    print(f'Steps: {area.step_count}')
    print(f'Trees: {area.tree_count}')


if __name__ == '__main__':
    main()
