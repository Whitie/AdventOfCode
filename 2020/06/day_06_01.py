#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'


def get_groups(filepath):
    with filepath.open() as fp:
        data = fp.read().split('\n\n')
    return [g.replace('\n', '').strip() for g in data]


def count(groups):
    return [len(set(g)) for g in groups]


def main():
    groups = get_groups(INPUT)
    yes_answers_combined = count(groups)
    print('Sum:', sum(yes_answers_combined))


if __name__ == '__main__':
    main()
