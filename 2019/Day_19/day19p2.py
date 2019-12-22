#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from queue import Empty

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


def inside(filename, x, y):
    ic = IntcodeComputer.from_file(filename)
    ic.write(y)
    ic.write(x)
    ic.run()
    return ic.output == 1


def main(filename):
    x = 0
    for y in range(100, 100000):
        while not inside(filename, x, y):
            x += 1
        if inside(filename, x+99, y-99):
            print(10000*x + (y-99))
            break


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
