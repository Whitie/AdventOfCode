#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

from collections import defaultdict


LINE_RE = re.compile(
    r'#(?P<id>\d+)\s+@\s+(?P<x>\d+),(?P<y>\d+):'
    r'\s+(?P<width>\d+)x(?P<height>\d+)'
)


def get_input(filename):
    inp = []
    with open(filename, 'r') as fp:
        for line in fp:
            line = line.strip()
            if line:
                inp.append(line)
    return inp


def fill_area(area, x, y, width, height):
    for row in range(y, y+height):
        for square in range(x, x+width):
            area[(square, row)] += 1
    return area


def check_overlapping(area, x, y, width, height):
    for row in range(y, y+height):
        for square in range(x, x+width):
            if area[(square, row)] != 1:
                return False
    return True


def main(filename):
    inp = get_input(filename)
    area = defaultdict(int)
    claims = []
    for line in inp:
        match = LINE_RE.search(line)
        if match:
            claims.append(tuple(map(int, match.groups())))
            area = fill_area(area, *claims[-1][1:])
    count = 0
    for square in area.values():
        if square > 1:
            count += 1
    print(f'Part 1: {count}')
    for claim in claims:
        if check_overlapping(area, *claim[1:]):
            print(f'Part 2: #{claim[0]}')
            break


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
