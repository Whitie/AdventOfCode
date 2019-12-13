#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from collections import defaultdict
from operator import itemgetter

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


INPUT_FILE = 'input.txt'


def chunks(iterable, size):
    it = list(iterable)
    for i in range(0, len(it), size):
        yield it[i:i+size]


def main(filename):
    ic = IntcodeComputer.from_file(filename)
    ic.run()
    out = ic.get_output()
    grid = defaultdict(int)
    for x, y, tile in chunks(out, 3):
        grid[(x, y)] = tile
    max_x, _ = max(grid.keys(), key=itemgetter(0))
    _, max_y = max(grid.keys(), key=itemgetter(1))
    print(max_x, max_y)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
