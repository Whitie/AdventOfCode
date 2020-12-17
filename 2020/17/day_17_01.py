#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

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


def parse(raw_data):
    grid = set()
    z = 0
    lines = raw_data.splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                grid.add((x, y, z))
    return ([[-1, len(lines[0])+1], [-1, len(lines)+1], [-1, 1]], grid)


def active_neighbors_nD(point, grid):
    count = 0
    for p in product(*(range(x-1, x+2) for x in point)):
        if p in grid and p != point:
            count += 1
    return count


def conway_step_nD(dims, grid):
    active = set()
    inactive = set()
    for point in product(*(range(*d) for d in dims)):
        neighs = active_neighbors_nD(point, grid)
        if point in grid:
            if not (neighs == 2 or neighs == 3):
                inactive |= reflections_xy(point)
        else:
            if neighs == 3:
                active |= reflections_xy(point)
    grid |= active
    grid -= inactive
    dims[0][0] -= 1
    dims[0][1] += 1
    dims[1][0] -= 1
    dims[1][1] += 1
    for i in range(2, len(dims)):
        dims[i][0] -= 1
    return (dims, grid)


def reflections_xy(point):
    x, y, *rest = point
    mirrors = product(*[(1, -1) for _ in range(len(rest))])
    return set((x, y, *tuple(map(operator.mul, mirror, rest)))
               for mirror in mirrors)


def solve1(data):
    dims, grid = data
    for _ in range(ROUNDS):
        dims, grid = conway_step_nD(dims, grid)
    return len(grid)


# def solve2(data):
#     dims, grid = data
#     grid = set([(x, y, z, 0) for x, y, z in grid])
#     dims = [*dims, [-1, 1]]
#     for _ in range(ROUNDS):
#         dims, grid = conway_step_nD(dims, grid)
#     return len(grid)


def main():
    # field = parse(TEST)
    field = parse(INPUT)
    print("Part 1: {}".format(solve1(field)))
    # print("Part 2: {}".format(solve2(field)))


if __name__ == "__main__":
    main()
