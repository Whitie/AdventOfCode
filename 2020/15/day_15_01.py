#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
ROUNDS = 2020
TEST1 = [0, 3, 6]  # 436
TEST2 = [1, 3, 2]  # 1
TEST3 = [2, 1, 3]  # 10
TEST4 = [3, 1, 2]  # 1836


def read_input(filepath):
    with filepath.open() as fp:
        return list(map(int, fp.read().strip().split(',')))


def main():
    # numbers = TEST4
    numbers = read_input(INPUT)
    positions = dict((n, i) for i, n in enumerate(numbers[:-1], start=1))
    for round in range(len(numbers), ROUNDS):
        last = numbers[-1]
        if last in positions:
            num = round - positions[last]
            numbers.append(num)
        else:
            numbers.append(0)
        positions[last] = round
    print(numbers[-1])


if __name__ == '__main__':
    main()
