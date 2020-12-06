#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def read_input(filepath):
    with filepath.open() as fp:
        return fp.read()


def get_groups(raw_input):
    data = raw_input.strip().split('\n\n')
    return [g.split('\n') for g in data]


def count(groups):
    yes_answers = []
    for group in groups:
        person = set(group[0])
        for p in group[1:]:
            person &= set(p)
        yes_answers.append(len(person))
    return yes_answers


def main():
    groups = get_groups(read_input(INPUT))
    yes_answers_combined = count(groups)
    print('Sum:', sum(yes_answers_combined))


if __name__ == '__main__':
    main()
