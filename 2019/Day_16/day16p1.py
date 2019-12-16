#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from operator import mul


BASE = [0, 1, 0, -1]


def cycle2(iterable):
    li = list(iterable)[:]
    for elem in li[1:]:
        yield elem
    while li:
        for elem in li:
            yield elem


def get_input(filename):
    with open(filename, 'r') as fp:
        data = fp.read().strip()
    return list(map(int, data))


def get_pattern(iteration=1):
    pattern = []
    for factor in BASE:
        pattern.extend([factor] * iteration)
    return pattern


def main(filename):
    inp = get_input(filename)
    print(inp)
    tmp = []
    count = 1
    while True:
        for elem, factor in zip(inp, cycle2(get_pattern(count))):
            tmp.append(abs(mul(elem, factor)) % 10)
        inp = tmp
        if count == 101:
            break
    print(tmp)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
