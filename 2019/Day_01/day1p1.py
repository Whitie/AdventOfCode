#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'


def main():
    with open('input.txt', 'r') as fp:
        modules = [int(line) for line in fp if line.strip()]
    print(modules, len(modules))
    tmp = []
    for mod in modules:
        tmp.append(mod // 3 - 2)
    print(tmp, len(tmp))
    print(sum(tmp))


if __name__ == '__main__':
    main()
