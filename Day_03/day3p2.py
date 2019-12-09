#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple


INPUT_FILE = 'input.txt'


Point = namedtuple('Point', 'x y')


class Line:

    def __init__(self, start, end):
        self.start = Point(*start)
        self.end = Point(*end)
        if self.start.x == self.end.x:
            step = 1 if self.end.y > self.start.y else -1
            self.points = [
                Point(self.start.x, y) for y in
                range(self.start.y, self.end.y, step)
            ]
        else:
            step = 1 if self.end.x > self.start.x else -1
            self.points = [
                Point(x, self.start.y) for x in
                range(self.start.x, self.end.x, step)
            ]
        self.steps = len(self.points)

    def __str__(self):
        return f'Line(start={self.start}, end={self.end})'

    __repr__ = __str__

    def intersect(self, line):
        point = set(self.points) & set(line.points)
        if point:
            p = point.pop()
            if p.x and p.y:
                return p
        raise ValueError('Linien haben keinen Schnittpunkt.')

    def steps_to(self, point):
        idx = self.points.index(point)
        return idx


def manhattan(point):
    return abs(point.x) + abs(point.y)


def get_wires(filename=INPUT_FILE):
    with open(filename, 'r') as fp:
        data = fp.read().strip()
    wire_1, wire_2 = data.split('\n', 2)
    return wire_1.split(','), wire_2.split(',')


def collect_lines(wire):
    pos = [0, 0]
    lines = []
    for item in wire:
        start = pos[:]
        direction = item[0]
        steps = int(item[1:])
        if direction == 'R':
            pos[0] += steps
        elif direction == 'L':
            pos[0] -= steps
        elif direction == 'U':
            pos[1] += steps
        elif direction == 'D':
            pos[1] -= steps
        else:
            raise ValueError(f'Unbekannte Richtung: {direction}')
        lines.append(Line(start, pos[:]))
    return lines


def main():
    w1, w2 = get_wires()
    wire_1 = collect_lines(w1)
    wire_2 = collect_lines(w2)
    points = []
    steps_1 = 0
    for line in wire_1:
        steps_2 = 0
        for l in wire_2:
            try:
                point = line.intersect(l)
                points.append(
                    (steps_1 + line.steps_to(point),
                     steps_2 + l.steps_to(point), point)
                )
                print('Schnittpunkt:', point)
            except ValueError:
                steps_2 += l.steps
        steps_1 += line.steps
    steps = set()
    for point in points:
        print(point, point[0] + point[1])
        steps.add(point[0] + point[1])
    print(min(steps))


if __name__ == '__main__':
    main()
