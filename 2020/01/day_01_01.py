#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations


INPUT = 'input_01.txt'
RESULT = 2020


def read_input():
    numbers = []
    with open(INPUT) as fp:
        for line in fp:
            if line.strip():
                numbers.append(int(line.strip()))
    return numbers


def main():
    numbers = read_input()
    for i, j in combinations(numbers, 2):
        if i + j == RESULT:
            print(f'{i} + {j} = {i+j}')
            print(f'{i} * {j} = {i*j}')


if __name__ == '__main__':
    main()
