#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from itertools import accumulate, cycle


PHASES = 100


def get_input(filename):
    with open(filename, 'r') as fp:
        return fp.read().strip()


def main(filename):
    inp = get_input(filename)
    offset = int(inp[:7])
    digits = [int(x) for x in inp]
    length = 10000 * len(digits) - offset
    it = cycle(reversed(digits))
    field = [next(it) for _ in range(length)]
    for _ in range(PHASES):
        field = [x % 10 for x in accumulate(field)]
    print(''.join(str(x) for x in field[-1:-9:-1]))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
