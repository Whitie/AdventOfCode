#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'


def main(data):
    print(data)
    data[1] = 12
    data[2] = 2
    pos = 0
    while True:
        if data[pos] == 99:
            break
        target = data[pos+3]
        source_1 = data[pos+1]
        source_2 = data[pos+2]
        if data[pos] == 1:
            data[target] = data[source_1] + data[source_2]
        elif data[pos] == 2:
            data[target] = data[source_1] * data[source_2]
        else:
            raise ValueError(f'Unbekannter OPCODE {data[pos]}')
        pos += 4
    print(data)
    print(data[0])


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = [int(x) for x in fp.read().split(',')]
    main(data)
