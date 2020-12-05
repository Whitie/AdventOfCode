#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST_INPUT = [
    'FBFBBFFRLR',  # (44, 5) 357
    'BFFFBBFRRR',  # (70, 7) 567
    'FFFBBBFRRR',  # (14, 7) 119
    'BBFFBBFRLL',  # (102, 4) 820
]


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


def partition(spec, count=128):
    whole = list(range(count))
    num = len(whole)
    for c in spec:
        num //= 2
        if c in 'FL':
            whole = whole[:num]
        else:
            whole = whole[num:]
    return whole[0]


def get_seat(ids, rows=128, columns=8):
    for row in range(rows):
        for column in range(columns):
            id = row * 8 + column
            if id not in ids:
                if id - 1 in ids and id + 1 in ids:
                    return id


def main():
    specs = read_input(INPUT)
    ids = []
    for spec in specs:
        row = partition(spec[:7])
        column = partition(spec[7:], 8)
        ids.append(row * 8 + column)
    print('Highest:', max(ids))
    seat_id = get_seat(ids)
    print(f'My seat ID: {seat_id}')


if __name__ == '__main__':
    main()
