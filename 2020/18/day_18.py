#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
""".strip().split('\n')


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


class NumberEqual(int):

    def __add__(self, other):
        return NumberEqual(int(self) + int(other))

    def __sub__(self, other):
        return NumberEqual(int(self) * int(other))

    @staticmethod
    def eval(expression):
        expression = expression.replace('*', '-')
        expr = re.sub(
            r'\d+',
            lambda m: f'NumberEqual({m.group(0)})',
            expression
        )
        return eval(expr)


class NumberReversed(int):

    def __add__(self, other):
        return NumberReversed(int(self) * int(other))

    def __mul__(self, other):
        return NumberReversed(int(self) + int(other))

    @staticmethod
    def eval(expression):
        expression = expression.replace('+', 'P')
        expression = expression.replace('*', '+')
        expression = expression.replace('P', '*')
        expr = re.sub(
            r'\d+',
            lambda m: f'NumberReversed({m.group(0)})',
            expression
        )
        return eval(expr)


def main():
    # inp = TEST
    inp = read_input(INPUT)
    print('Part 1:', sum(map(NumberEqual.eval, inp)))
    print('Part 2:', sum(map(NumberReversed.eval, inp)))


if __name__ == '__main__':
    main()
