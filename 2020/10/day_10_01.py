#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from itertools import combinations
from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST1 = PATH / 'test1.txt'
TEST2 = PATH / 'test2.txt'


def read_input(filepath):
    with filepath.open() as fp:
        return [int(line) for line in fp if line.strip()]


def main():
    jolts = read_input(INPUT)
    #jolts = read_input(TEST2)
    jolts = list(sorted(jolts))
    jolts.insert(0, 0)
    diffs = {1: 0, 3: 1}
    for i, jolt in enumerate(jolts[1:]):
        diff = jolt - jolts[i]
        diffs[diff] += 1
    print(diffs, diffs[1] * diffs[3])


if __name__ == '__main__':
    main()
