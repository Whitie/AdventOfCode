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
    for i, j, k in combinations(numbers, 3):
        if i + j + k == RESULT:
            print(f'{i} + {j} + {k} = {i+j+k}')
            print(f'{i} * {j} * {k} = {i*j*k}')


if __name__ == '__main__':
    main()
