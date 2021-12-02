#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST1 = '7,13,x,x,59,x,31,19'.split(',')
TEST2 = '17,x,13,19'.split(',')


def read_input(filepath):
    with filepath.open() as fp:
        data = [line.strip() for line in fp if line.strip()]
    return data[1].split(',')


def get_offsets(departs):
    bus_ids = []
    offsets = []
    for i, item in enumerate(departs):
        if item != 'x':
            bus_ids.append(int(item))
            offsets.append(i)
    return bus_ids, offsets


def check_times(times, offsets):
    for i in range(1, len(times)):
        if times[i] - times[0] != offsets[i]:
            return False
    return True


def main():
    bus_ids, offsets = get_offsets(TEST2)
    # bus_ids, offsets = get_offsets(read_input(INPUT))
    t = 0
    times = offsets[:]
    while True:
        for i in range(len(bus_ids)):
            if t % bus_ids[i] == offsets[i]:
                times[i] += bus_ids[i]
        if check_times(times, offsets):
            break
        t += 1
    print(bus_ids)
    print(offsets)
    print(times)
    print(t)


if __name__ == '__main__':
    main()
