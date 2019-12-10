#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys

from collections import defaultdict, namedtuple


Point = namedtuple('Point', 'x y')


def read_file(filename):
    coordinates = []
    with open(filename, 'r') as fp:
        for y, line in enumerate(fp):
            line = line.strip()
            if line:
                for x, place in enumerate(line):
                    if place == '#':
                        coordinates.append(Point(x, y))
    return coordinates


def angle(point_1, point_2):
    return math.atan2(point_1.y - point_2.y, point_1.x - point_2.x)


def main(filename):
    asteroids = read_file(filename)
    # print(asteroids)
    angles = defaultdict(set)
    for asteroid_1 in asteroids:
        for asteroid_2 in asteroids:
            if asteroid_1 == asteroid_2:
                continue
            angles[asteroid_1].add(angle(asteroid_1, asteroid_2))
    point = None
    count = 0
    for asteroid, angles_ in angles.items():
        a_count = len(angles_)
        if a_count > count:
            point = asteroid
            count = a_count
    print(f'X: {point.x}, Y: {point.y} DETECTION: {count}')


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
