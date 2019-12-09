#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'


def calculate_fuel(module):
    fuel = 0
    while True:
        current = module // 3 - 2
        if current > 0:
            fuel += current
            module = current
        else:
            return fuel


def main():
    with open('input.txt', 'r') as fp:
        modules = [int(line) for line in fp if line.strip()]
    print(modules, len(modules))
    tmp = []
    for mod in modules:
        tmp.append(calculate_fuel(mod))
    print(tmp, len(tmp))
    print(sum(tmp))


if __name__ == '__main__':
    main()
