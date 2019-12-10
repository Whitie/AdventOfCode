#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys

from collections import namedtuple
from operator import itemgetter

from day10p1 import main as part_1_main


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
    d_x = point_2.x - point_1.x
    d_y = point_2.y - point_1.y
    rads = math.atan2(d_x, -d_y)
    degs = math.degrees(rads)
    if degs < 0:
        degs = 360 + degs
    return degs


def distance(point_1, point_2):
    return ((point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2)**0.5


def vaporize(point, locations):
    points = []
    for location in locations:
        dist = distance(location, point)
        ang = angle(point, location)
        points.append((location, ang, dist))
    points.sort(key=itemgetter(1, 2), reverse=True)
    to_remove = len(points) - 1
    p_angle = -1
    count = 0
    while True:
        angle_ = points[to_remove][1]
        if angle_ != p_angle or len(points) <= 1:
            p_point, _, _ = points.pop(to_remove)
            count += 1
            if count == 200:
                return p_point.x * 100 + p_point.y
        p_angle = angle_
        to_remove -= 1
        if to_remove < 0:
            to_remove = len(points) - 1


def main(filename):
    asteroids = read_file(filename)
    _, best_point = part_1_main(filename)
    asteroids.remove(best_point)
    return vaporize(best_point, asteroids)


if __name__ == '__main__':
    try:
        result = main(sys.argv[1])
        print(f'Result on position 200: {result}')
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
