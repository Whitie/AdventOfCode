#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
from itertools import product


ROUNDS = 6
TEST = """
.#.
..#
###
""".strip()
INPUT = """
.##...#.
.#.###..
..##.#.#
##...#.#
#..#...#
#..###..
.##.####
..#####.
""".strip()


class Vector(tuple):

    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __add__(self, other):
        return Vector(*tuple(a + b for a, b in zip(self, other)))


def get_neighbours(pos, dimension):
    for delta in product(range(-1, 2), repeat=dimension):
        if all(x == 0 for x in delta):
            continue
        yield pos + Vector(*delta)


def solve(lines, dimension):
    field = set()
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell != '#':
                continue
            if dimension == 3:
                field.add(Vector(x, y, 0))
            else:
                field.add(Vector(x, y, 0, 0))
    for _ in range(ROUNDS):
        neighbours = Counter([p for pos in field for p in
                              get_neighbours(pos, dimension)])
        field = {pos for pos, count in neighbours.items()
                 if count == 3 or (count == 2 and pos in field)}
    return len(field)


def main():
    # lines = TEST.split('\n')
    lines = INPUT.split('\n')
    print('Part 1:', solve(lines, 3))
    print('Part 2:', solve(lines, 4))


if __name__ == "__main__":
    main()
