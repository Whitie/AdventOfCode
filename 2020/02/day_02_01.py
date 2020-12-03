#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT = 'input.txt'
# 410

def read_input():
    with open(INPUT) as fp:
        for line in fp:
            if line.strip():
                yield line.strip().split(' ', 3)


def _get_times(policy):
    start, end = map(int, policy.split('-'))
    return range(start, end+1)


def main():
    valid = 0
    for policy, char, password in read_input():
        times = _get_times(policy)
        if password.count(char.strip(':')) in times:
            valid += 1
    print(f'Valid passwords: {valid}')


if __name__ == '__main__':
    main()
