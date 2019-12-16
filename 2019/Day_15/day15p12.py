#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from threading import Thread

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


INPUT_FILE = 'input.txt'
NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4
REVERSE_MOVES = {NORTH: SOUTH, SOUTH: NORTH, WEST: EAST, EAST: WEST}
DELTA = {NORTH: (-1, 0), SOUTH: (1, 0), WEST: (0, -1), EAST: (0, 1)}


def tuple_add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


class Droid:

    def __init__(self, program_file):
        self.ic = IntcodeComputer.from_file(program_file)
        self.vm = Thread(target=self.ic.run)
        self.seen = {}
        self.oxygen = {}
        self.to_fill = None
        self._in = self.ic.in_queue.put
        self._out = self.ic.out_queue.get
        self.vm.start()

    def step(self, inp):
        self._in(inp)
        return self._out()

    def find(self, pos=(0, 0), steps=0):
        found = None
        for i in range(1, 5):
            new_pos = tuple_add(pos, DELTA[i])
            if new_pos in self.seen:
                continue
            self.seen[new_pos] = self.step(i)
            if self.seen[new_pos] == 2:
                found = pos, steps + 1
            elif self.seen[new_pos] == 1:
                res = self.find(tuple_add(pos, DELTA[i]), steps + 1)
                if res:
                    found = res
            if self.seen[new_pos] in (1, 2):
                self.step(REVERSE_MOVES[i])
        return found

    def fill(self, pos, time):
        if pos in self.oxygen:
            return
        if pos in self.seen and self.seen[pos] in (1, 2):
            self.oxygen[pos] = time
            for step in range(1, 5):
                self.to_fill.add((tuple_add(pos, DELTA[step]), time + 1))


def main(filename):
    droid = Droid(filename)
    pos, num = droid.find()
    print(f'Fewest movements: {num}')
    droid.to_fill = {(pos, 1)}
    while droid.to_fill:
        p, t = droid.to_fill.pop()
        droid.fill(p, t)
    minutes = max(droid.oxygen.values())
    print(f'Minutes to fill: {minutes}')


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
