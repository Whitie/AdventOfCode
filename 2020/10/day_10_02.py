#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST1 = PATH / 'test1.txt'
TEST2 = PATH / 'test2.txt'


def read_input(filepath):
    with filepath.open() as fp:
        return [int(line) for line in fp if line.strip()]


def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    jolts = read_input(INPUT)
    #jolts = read_input(TEST2)
    jolts = list(sorted(jolts))
    jolts.insert(0, 0)
    jolts.append(max(jolts) + 3)
    diffs = [jolts[i] - jolts[i-1] for i in range(1, len(jolts))]
    factors = [1] + [sum(fib(x)) for x in range(10)][2:]
    i = 0
    res = 1
    while i < len(diffs):
        in_row = 0
        while diffs[i] == 1:
            in_row += 1
            i += 1
        res *= factors[in_row]
        i += 1
    print(res)


if __name__ == '__main__':
    main()
