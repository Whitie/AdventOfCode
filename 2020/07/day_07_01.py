#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


def split_line(line):
    return line.split(' contain ')


def can_contain(bags, content):
    for bag in bags:
        if bag in content:
            return True
    return False


def check_bags(inp, bags):
    new_bags = set()
    for line in inp:
        bag, content = split_line(line)
        if can_contain(bags, content):
            new_bags.add(bag.rsplit(' ', 1)[0])
    return new_bags


def main():
    bags = {BAG}
    inp = read_input(INPUT)
    # inp = TEST
    while True:
        count = len(bags)
        bags |= check_bags(inp, bags)
        if count == len(bags):
            break
    print(len(bags) - 1)


if __name__ == '__main__':
    main()
