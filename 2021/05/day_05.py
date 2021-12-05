#!/usr/bin/python

from collections import defaultdict


def get_input(filename):
    data = []
    with open(filename) as fp:
        for line in fp:
            if line.strip():
                start, end = line.split('->')
                x1, y1 = start.split(',')
                x2, y2 = end.split(',')
                data.append([(int(x1), int(y1)), (int(x2), int(y2))])
    return data


def a():
    data = get_input('input_05.txt')
    vents = defaultdict(int)
    for start, end in data:
        start_x = min([start[0], end[0]])
        end_x = max([start[0], end[0]])
        start_y = min([start[1], end[1]])
        end_y = max([start[1], end[1]])
        if start[0] == end[0]:
            for i in range(start_y, end_y + 1):
                vents[(start[0], i)] += 1
        if start[1] == end[1]:
            for i in range(start_x, end_x + 1):
                vents[(i, start[1])] += 1
    points = 0
    for point in vents.values():
        if point >= 2:
            points += 1
    print(points)


def b():
    data = get_input('input_05.txt')
    vents = defaultdict(int)
    for start, end in data:
        start_x = min([start[0], end[0]])
        end_x = max([start[0], end[0]])
        start_y = min([start[1], end[1]])
        end_y = max([start[1], end[1]])
        if start[0] == end[0]:
            for i in range(start_y, end_y + 1):
                vents[(start[0], i)] += 1
        if start[1] == end[1]:
            for i in range(start_x, end_x + 1):
                vents[(i, start[1])] += 1
        if (
            abs(start[0] - start[1]) == abs(end[0] - end[1])
            or start[0] + start[1] == end[0] + end[1]
        ):
            print('dia')
            if start[0] > end[0]:
                end_x = end[0] - 1
                step_x = -1
            else:
                end_x = end[0] + 1
                step_x = 1
            if start[1] > end[1]:
                end_y = end[1] - 1
                step_y = -1
            else:
                end_y = end[1] + 1
                step_y = 1
            for x, y in zip(
                range(start[0], end_x, step_x),
                range(start[1], end_y, step_y)
            ):
                vents[(x, y)] += 1
    points = 0
    for point in vents.values():
        if point >= 2:
            points += 1
    print(points)


def main():
    a()
    b()


if __name__ == '__main__':
    main()
