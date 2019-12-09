#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
    raise Exception('Keine doppelte Nummer')


def _check_increase_or_stay(num):
    nums = tuple(map(int, str(num)))
    if nums[0] <= nums[1] <= nums[2] <= nums[3] <= nums[4] <= nums[5]:
        return
    raise Exception(f'Nicht ansteigend oder gleich: {num}')


def check_number(num):
    _check_digits(num, 6)
    _check_double(num)
    _check_increase_or_stay(num)
    return num


def main():
    low, high = tuple(map(int, INPUT.split('-')))
    possible = set()
    for num in range(low, high + 1):
        try:
            possible.add(check_number(num))
            print('Möglich:', num)
        except Exception:
            pass
    print(len(possible))


if __name__ == '__main__':
    main()
