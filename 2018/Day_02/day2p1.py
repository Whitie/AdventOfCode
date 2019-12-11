#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from collections import defaultdict


def get_input(filename):
    inp = []
    with open(filename, 'r') as fp:
        for line in fp:
            line = line.strip()
            if line:
                inp.append(line)
    return inp


def count_chars(line):
    counter = defaultdict(int)
    for char in line:
        counter[char] += 1
    two = 2 in counter.values()
    three = 3 in counter.values()
    return int(two), int(three)


def main(filename):
    inp = get_input(filename)
    times = [0, 0]
    for line in inp:
        two, three = count_chars(line)
        times[0] += two
        times[1] += three
    result = times[0] * times[1]
    print(f'2x {times[0]}, 3x {times[1]}, result: {result}')


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
