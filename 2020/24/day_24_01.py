#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = PATH / 'test.txt'
MOVE_RE = re.compile(r'w|e|se|sw|ne|nw', re.I)
MOVES = {
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
}


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


def _move(move, pos):
    x, y = pos
    dx, dy = MOVES[move]
    return (x + dx, y + dy)


def main():
    # lines = read_input(TEST)
    lines = read_input(INPUT)
    black_tiles = set()
    for line in lines:
        pos = (0, 0)
        for move in MOVE_RE.findall(line):
            pos = _move(move, pos)
        black_tiles ^= {pos}
    print(len(black_tiles))


if __name__ == '__main__':
    main()
