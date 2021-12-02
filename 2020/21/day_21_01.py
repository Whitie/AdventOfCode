#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip().splitlines()


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


def parse_list(raw):
    tmp = []
    for line in raw:
        i, a = line.split('(')
        a = a.split(' ', 1)[1]
        ing = set([x.strip() for x in i.split()])
        allergens = set([x.strip() for x in a.split(',')])
        tmp.append((ing, allergens))
    return tmp


def main():
    ing = parse_list(TEST)
    # ing = parse_list(read_input(INPUT))
    print(ing[0])


if __name__ == '__main__':
    main()
