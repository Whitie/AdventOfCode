#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """
F10
N3
F7
R90
F11
""".strip().split('\n')


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


def parse_commands(commands):
    parsed = []
    for command in commands:
        parsed.append((command[0], int(command[1:])))
    return parsed


def main():
    # commands = parse_commands(TEST)
    commands = parse_commands(read_input(INPUT))
    directions = ['E', 'S', 'W', 'N']
    direction = 'E'
    steps = dict(N=0, E=0, W=0, S=0)
    for command, value in commands:
        if command in 'EWNS':
            steps[command] += value
        elif command == 'F':
            steps[direction] += value
        elif command in 'LR':
            if command == 'L':
                tmp = directions.index(direction) - value // 90
            else:
                tmp = directions.index(direction) + value // 90
            direction = directions[tmp % 4]
    print(steps)
    print(abs(steps['N'] - steps['S']), abs(steps['E'] - steps['W']))
    print(abs(steps['N'] - steps['S']) + abs(steps['E'] - steps['W']))


if __name__ == '__main__':
    main()
