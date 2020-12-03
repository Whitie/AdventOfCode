#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT = 'input.txt'
# 694

def read_input():
    with open(INPUT) as fp:
        for line in fp:
            if line.strip():
                yield line.strip().split(' ', 3)


def main():
    valid = 0
    for policy, char, password in read_input():
        positions = tuple(map(int, policy.split('-')))
        first, second = positions[0] - 1, positions[1] - 1
        char = char.strip(':')
        if password[first] == char or password[second] == char:
            if password[first] == char and password[second] == char:
                continue
            else:
                valid += 1
    print(f'Valid passwords: {valid}')


if __name__ == '__main__':
    main()
