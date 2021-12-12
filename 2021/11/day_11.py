#!/usr/bin/python

TEST = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
INPUT = """\
1564524226
1384554685
7582264835
8812672272
1161463137
7831762344
2855527748
6141737874
8611458313
8215372443
"""


def get_input(inp=TEST):
    data = {}
    for y, line in enumerate(inp.strip().split('\n')):
        for x, level in enumerate(line):
            data[(x, y)] = int(level)
    return data


def increase_level(data):
    for key in data.keys():
        data[key] += 1
    return data


def increase_adjacents(x, y, data):
    adjacents = (
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1),
    )
    for pos in adjacents:
        try:
            data[pos] += 1
        except KeyError:
            pass
    return data


def flash(data):
    flashed = []
    new = True
    while new:
        new = False
        new_flashed = []
        for key in data.keys():
            if data[key] > 9 and key not in flashed:
                flashed.append(key)
                new_flashed.append(key)
                new = True
        for x, y in new_flashed:
            data = increase_adjacents(x, y, data)
    for key in flashed:
        data[key] = 0
    return data, len(flashed)


def a():
    data = get_input(INPUT)
    sum_ = 0
    for i in range(100):
        print('Step', i+1, end=' ')
        data = increase_level(data)
        data, flashed = flash(data)
        print(flashed)
        sum_ += flashed
    print(sum_)


def b():
    data = get_input(INPUT)
    step = 0
    while True:
        print('Step', step+1, end=' ')
        data = increase_level(data)
        data, flashed = flash(data)
        step += 1
        print(flashed)
        if flashed == len(data):
            break
    print(step)


def main():
    a()
    b()


if __name__ == '__main__':
    main()
