#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'


def get_path(orbits, start, to='COM'):
    path = []
    item = orbits[start]
    while item != to:
        path.append(item)
        item = orbits[item]
    return list(reversed(path))


def get_same_count(path_1, path_2):
    for count, pair in enumerate(zip(path_1, path_2)):
        if pair[0] != pair[1]:
            break
    return count


def main():
    with open(INPUT_FILE, 'r') as fp:
        lines = [x.strip().split(')') for x in fp]
    orbits = {val: key for key, val in lines}
    you_path = get_path(orbits, 'YOU')
    san_path = get_path(orbits, 'SAN')
    same_count = get_same_count(you_path, san_path)
    print(same_count)
    print(len(you_path[same_count:]) + len(san_path[same_count:]))


if __name__ == '__main__':
    main()
