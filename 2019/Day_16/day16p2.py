#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


BASE = [0, 1, 0, -1]
PHASES = 100


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


def calculate_one_line(inp, iteration):
    pattern = get_pattern(iteration)
    tmp = []
    for elem, factor in zip(inp, cycle2(pattern)):
        tmp.append(elem * factor)
    return sum(tmp)


def calculate_one_phase(inp):
    phase = []
    for i in range(1, len(inp) + 1):
        res = calculate_one_line(inp, i)
        phase.append(abs(res) % 10)
    return phase


def main(filename):
    inp = get_input(filename)
    offset = int(''.join([str(x) for x in inp[:7]]))
    print('This takes tooo long...')
    inp = inp * 10000
    for i in range(PHASES):
        phase = calculate_one_phase(inp)
        print(f'{i+1}) {phase[:8]}')
        inp = phase
    print(''.join([str(x) for x in phase[offset:offset+8]]))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
