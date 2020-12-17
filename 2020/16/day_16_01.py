#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip()


def read_input(filepath):
    with filepath.open() as fp:
        return fp.read().strip()


def _parse_sets(sets):
    nums = set()
    for s in sets:
        start, end = list(map(int, s.split('-')))
        nums |= set(range(start, end+1))
    return nums


def _parse_defs(raw):
    definitions = {}
    for line in raw.split('\n'):
        name, defs = line.split(':')
        definitions[name.strip()] = _parse_sets(defs.split('or'))
    return definitions


def _parse_tickets(raw):
    numbers = []
    for line in raw.split('\n')[1:]:
        numbers.extend(list(map(int, line.split(','))))
    return numbers


def parse_input(raw):
    content = raw.split('\n\n', 3)
    defs = _parse_defs(content[0])
    my_ticket = _parse_tickets(content[1])
    tickets = _parse_tickets(content[2])
    return defs, my_ticket, tickets


def is_valid(number, defs):
    for range_ in defs.values():
        if number in range_:
            return True
    return False


def main():
    # inp = TEST
    inp = read_input(INPUT)
    defs, _, tickets = parse_input(inp)
    invalid = []
    for number in tickets:
        if not is_valid(number, defs):
            invalid.append(number)
    print(invalid)
    print(sum(invalid))


if __name__ == '__main__':
    main()
