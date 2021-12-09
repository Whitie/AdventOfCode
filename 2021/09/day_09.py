#!/usr/bin/python

from collections import defaultdict


TEST = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def get_ten():
    return 10


def get_input():
    data = defaultdict(get_ten)
    height = 0
    with open('input_09.txt') as fp:
        for y, line in enumerate(fp):
            line = line.strip()
            if line:
                height += 1
                width = len(line)
                for x, number in enumerate(line):
                    data[(x, y)] = int(number)
    return width, height, data


def get_test_input():
    data = defaultdict(get_ten)
    height = 0
    for y, line in enumerate(TEST.split('\n')):
        line = line.strip()
        if line:
            height += 1
            width = len(line)
            for x, number in enumerate(line):
                data[(x, y)] = int(number)
    return width, height, data


def check(x, y, data):
    value = data[(x, y)]
    adjacents = [data[(x-1, y)], data[(x+1, y)], data[(x, y-1)],
                 data[(x, y+1)]]
    return min(adjacents) > value


def a():
    w, h, data = get_input()
    print(f'Width: {w}, Height: {h}')
    sum_ = 0
    for y in range(h):
        for x in range(w):
            if check(x, y, data):
                sum_ += 1 + data[(x, y)]
    print(sum_)


def b():
    pass


def main():
    a()
    b()


if __name__ == '__main__':
    main()
