#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from collections import deque
from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
BAG = 'shiny gold'
TEST = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip().split('\n')
TEST2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".strip().split('\n')


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


def count_inside(colors, which):
    if not len(colors[which]):
        return 1
    sum_ = 1
    for x in colors[which]:
        sum_ += int(colors[which][x]) * count_inside(colors, x)
    return sum_


def main():
    data = read_input(INPUT)
    # data = TEST
    colors = {}
    for line in data:
        parts = line.split()
        color = f'{parts[0]} {parts[1]}'
        colors[color] = {}
        i = 2
        while i < len(parts):
            if re.match(r'\d+', parts[i]):
                new_color = f'{parts[i+1]} {parts[i+2]}'
                colors[color][new_color] = parts[i]
            i += 1
    print(count_inside(colors, BAG) - 1)


if __name__ == '__main__':
    main()
