#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'


def main():
    frequency = 0
    frequencies = []
    seen = {0}
    with open(INPUT_FILE, 'r') as fp:
        for line in fp:
            l = line.strip()
            if l:
                frequencies.append(int(l))
    not_seen = True
    while not_seen:
        for f in frequencies:
            frequency += f
            if frequency in seen:
                not_seen = False
                break
            else:
                seen.add(frequency)
    print(len(frequencies))
    print(f'Frequency: {frequency}')


if __name__ == '__main__':
    main()
