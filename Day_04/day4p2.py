#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict


INPUT = '171309-643603'


def _check_digits(num, length):
    if len(str(num)) != length:
        raise Exception(f'Länge ist nicht {length}: {num}')


def _check_double(num):
    n = str(num)
    if (
        n[0] == n[1] or n[1] == n[2] or n[2] == n[3]
        or n[3] == n[4] or n[4] == n[5]
    ):
        return
    raise Exception(f'Keine doppelte Nummer: {num}')


def _check_increase_or_stay(num):
    nums = tuple(map(int, str(num)))
    if nums[0] <= nums[1] <= nums[2] <= nums[3] <= nums[4] <= nums[5]:
        return
    raise Exception(f'Nicht ansteigend oder gleich: {num}')


def _check_triple(num):
    number = str(num)
    d = defaultdict(int)
    for n in number:
        d[n] += 1
    has_double = False
    multi = False
    for v in d.values():
        if v == 2:
            has_double = True
        if v > 2:
            multi = True
    if multi and not has_double:
        raise Exception(f'Vielfaches (drei oder mehr) gefunden: {num}')


def check_number(num):
    _check_digits(num, 6)
    _check_double(num)
    _check_increase_or_stay(num)
    _check_triple(num)
    return num


def main():
    low, high = tuple(map(int, INPUT.split('-')))
    possible = set()
    for num in range(low, high + 1):
        try:
            possible.add(check_number(num))
            print('Möglich:', num)
        except Exception as err:
            pass
    print(len(possible))


if __name__ == '__main__':
    main()
