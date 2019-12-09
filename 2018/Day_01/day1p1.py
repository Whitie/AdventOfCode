#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'


def main():
    frequency = 0
    with open(INPUT_FILE, 'r') as fp:
        for line in fp:
            l = line.strip()
            if l:
                frequency += int(l)
    print(f'Frequency: {frequency}')


if __name__ == '__main__':
    main()
