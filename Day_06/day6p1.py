#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as fp:
        lines = [x.strip().split(')') for x in fp]
    orbits = {val: key for key, val in lines}
    count = 0
    for item in orbits:
        obj = item
        while obj in orbits:
            obj = orbits[obj]
            count += 1
    print(count)


if __name__ == '__main__':
    main()
