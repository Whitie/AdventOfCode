#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
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
        numbers.append(list(map(int, line.split(','))))
    return numbers


def parse_input(raw):
    content = raw.split('\n\n', 3)
    defs = _parse_defs(content[0])
    my_ticket = _parse_tickets(content[1])[0]
    tickets = _parse_tickets(content[2])
    return defs, my_ticket, tickets


def is_valid(number, defs):
    for range_ in defs.values():
        if number in range_:
            return True
    return False


def _get_only_valid(tickets, defs):
    valid = []
    for ticket in tickets:
        for number in ticket:
            if not is_valid(number, defs):
                break
        else:
            valid.append(ticket)
    return valid


def main():
    inp = TEST
    # inp = read_input(INPUT)
    defs, _, tickets = parse_input(inp)
    valid_tickets = _get_only_valid(tickets, defs)
    print(len(valid_tickets))


if __name__ == '__main__':
    main()
