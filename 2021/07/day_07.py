#!/usr/bin/python


def get_input(filename):
    with open(filename) as fp:
        data = fp.read().strip()
    return list(map(int, data.split(',')))


def a():
    data = get_input('input_07.txt')
    print(min(data), max(data), len(data))
    data.sort()
    middle = len(data) // 2
    fuel = 0
    for pos in data:
        fuel += abs(data[middle] - pos)
    print(fuel)


def _gauss(x):
    return (x * (x + 1)) / 2


# From Reddit:

def b():
    data = get_input('input_07.txt')
    print(min([
        sum([_gauss(abs(x - target)) for x in data])
        for target in range(max(data))
    ]))


def main():
    a()
    b()


if __name__ == '__main__':
    main()
