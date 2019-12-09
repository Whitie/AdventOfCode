#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'
OUTPUT = 19690720


def run(data, noun=12, verb=2):
    #print(data)
    data[1] = noun
    data[2] = verb
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
    #print(data)
    return data[0]


def main(data):
    for i in range(100):
        for j in range(100):
            if run(data[:], i, j) == OUTPUT:
                return i, j


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = [int(x) for x in fp.read().split(',')]
    noun, verb = main(data)
    print(noun, verb)
    print(100 * noun + verb)
