#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


def is_intersection(x, y, field):
    positions = ((x, y-1), (x-1, y), (x+1, y), (x, y+1))
    for x, y in positions:
        if x < 1 or y < 1:
            return False
        try:
            if field[y][x] != '#':
                return False
        except IndexError:
            return False
    return True


def main(filename):
    ic = IntcodeComputer.from_file(filename)
    ic.run()
    field = []
    line = []
    for i in ic.get_output():
        if i == 10:
            field.append(line[:])
            line = []
        else:
            line.append(chr(i))
    for i, line in enumerate(field):
        print(f'{i:2d}', ''.join(line))
    align = []
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == '#' and is_intersection(x, y, field):
                print(f'FOUND: X: {x}, Y: {y}')
                align.append(x * y)
    print(sum(align))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
