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
    cardinals = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    ship = 0, 0
    waypoint = 10, 1
    for action, value in commands:
        if action in cardinals:
            waypoint = (waypoint[0] + value * cardinals[action][0],
                        waypoint[1] + value * cardinals[action][1])
        elif action == 'F':
            ship = (ship[0] + value * waypoint[0],
                    ship[1] + value * waypoint[1])
        else:
            x, y = waypoint
            clockwise_degrees = {'L': 360 - value, 'R': value}[action]
            waypoint = {
                90: (y, -x),
                180: (-x, -y),
                270: (-y, x)
            }[clockwise_degrees]
    print(sum(map(abs, ship)))


if __name__ == '__main__':
    main()
