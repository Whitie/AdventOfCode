#!/usr/bin/python


def iter_input(filename):
    with open(filename) as fp:
        for line in fp:
            if line.strip():
                command, value = line.strip().split()
                yield command, int(value)


def a(filename):
    position = 0
    depth = 0
    for command, value in iter_input(filename):
        if command == 'forward':
            position += value
        elif command == 'down':
            depth += value
        elif command == 'up':
            depth -= value
    print(f'Position: {position}, Depth: {depth}')
    print(position * depth)


def b(filename):
    position = 0
    depth = 0
    aim = 0
    for command, value in iter_input(filename):
        if command == 'forward':
            position += value
            depth += aim * value
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value
    print(f'Position: {position}, Depth: {depth}, Aim: {aim}')
    print(position * depth)


def main():
    filename = 'input_02.txt'
    a(filename)
    b(filename)


if __name__ == '__main__':
    main()
