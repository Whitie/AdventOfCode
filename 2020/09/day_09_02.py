#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from itertools import combinations
from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST1 = PATH / 'test1.txt'


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


def get_first_invalid(numbers, preamble):
    previous = deque(numbers[:preamble], maxlen=preamble)
    for i, number in enumerate(numbers[preamble:], start=preamble):
        sums = map(sum, combinations(previous, 2))
        if number not in sums:
            return i, number
        previous.append(number)


def main():
    #numbers, preamble = list(map(int, read_input(TEST1))), 5
    numbers, preamble = list(map(int, read_input(INPUT))), 25
    index, number = get_first_invalid(numbers, preamble)
    numbers = numbers[:index]
    loop = 0
    end = False
    while not end:
        sum_ = 0
        inner = loop
        for value in numbers[loop:]:
            sum_ += value
            if sum_ == number:
                set_ = numbers[loop:inner]
                xmas = min(set_) + max(set_)
                print(f'{min(set_)} + {max(set_)} = {xmas}')
                end = True
                break
            elif sum_ > number:
                break
            inner += 1
        loop += 1


if __name__ == '__main__':
    main()
