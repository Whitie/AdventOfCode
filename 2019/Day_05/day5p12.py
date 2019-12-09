#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT_FILE = 'input.txt'

OPCODE_LENGTH = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
}


def _parse_instruction(instruction):
    opcode = instruction % 100
    modes = list(map(int, str(instruction)[:-2]))
    if len(modes) < 3:
        while len(modes) < 3:
            modes.insert(0, 0)
    return opcode, tuple(reversed(modes))


def main(data):
    pos = 0
    while True:
        opcode, modes = _parse_instruction(data[pos])
        jump = False
        if opcode == 99:
            break
        if modes[0] == 0:
            source_1 = data[pos+1]
        else:
            source_1 = pos + 1
        if opcode in (1, 2, 7, 8):
            if modes[1] == 0:
                source_2 = data[pos+2]
            else:
                source_2 = pos + 2
            if modes[2] == 0:
                target = data[pos+3]
            else:
                target = pos + 3
            if opcode == 1:
                data[target] = data[source_1] + data[source_2]
            elif opcode == 2:
                data[target] = data[source_1] * data[source_2]
            elif opcode == 7:
                if data[source_1] < data[source_2]:
                    data[target] = 1
                else:
                    data[target] = 0
            elif opcode == 8:
                if data[source_1] == data[source_2]:
                    data[target] = 1
                else:
                    data[target] = 0
        elif opcode in (3, 4):
            if opcode == 3:
                data[source_1] = int(input('Zahl: '))
            else:
                print(data[source_1])
        elif opcode in (5, 6):
            if modes[1] == 0:
                source_2 = data[pos+2]
            else:
                source_2 = pos + 2
            if opcode == 5:
                if data[source_1]:
                    pos = data[source_2]
                    jump = True
            elif opcode == 6:
                if data[source_1] == 0:
                    pos = data[source_2]
                    jump = True
        else:
            raise ValueError(f'Unbekannter OPCODE {data[pos]}')
        if not jump:
            pos += OPCODE_LENGTH[opcode]


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = [int(x) for x in fp.read().split(',')]
    main(data)
