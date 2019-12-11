#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from collections import defaultdict
from operator import itemgetter
from queue import Queue
from threading import Thread

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


class Panel:
    BLACK = 0
    WHITE = 1

    def __init__(self):
        self.color = self.BLACK
        self.count = 0

    def __str__(self):
        return '#' if self.color else '.'


class Robot:
    DIRECTIONS = '^>v<'

    def __init__(self, x=0, y=0, direction='^'):
        self.x = x
        self.y = y
        self.direction = direction

    @property
    def position(self):
        return self.x, self.y

    def _move(self):
        if self.direction == '^':
            self.y += 1
        elif self.direction == '>':
            self.x += 1
        elif self.direction == 'v':
            self.y -= 1
        else:
            self.x -= 1

    def move(self, new_direction):
        pos = self.DIRECTIONS.find(self.direction)
        if new_direction:
            pos += 1
        else:
            pos -= 1
        pos %= 4
        self.direction = self.DIRECTIONS[pos]
        self._move()


def print_hull(hull, robot):
    keys = hull.keys()
    min_x, max_x = min(keys, key=itemgetter(0))[0], max(keys, key=itemgetter(0))[0]
    min_y, max_y = min(keys, key=itemgetter(1))[1], max(keys, key=itemgetter(1))[1]
    for row in range(max_y, min_y, -1):
        print()
        for panel in range(min_x, max_x):
            pos = panel, row
            if robot.position == pos:
                print(robot.direction, end='')
            else:
                print(hull[pos], end='')
    print()


def main(filename):
    out = Queue()
    hull = defaultdict(Panel)
    with open(filename, 'r') as fp:
        ic = IntcodeComputer(fp.read(), out_queue=out, init=0)
    ic_thread = Thread(target=ic.run)
    ic_thread.start()
    robot = Robot()
    while True:
        if ic.halt:
            break
        color = out.get()
        hull[robot.position].color = color
        hull[robot.position].count += 1
        direction = out.get()
        robot.move(direction)
        ic.in_queue.put(hull[robot.position].color)
    print_hull(hull, robot)
    count = 0
    for pos, panel in hull.items():
        if panel.count >= 1:
            count += 1
    print(f'Painted once: {count}')


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
