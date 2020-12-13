#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = (939, [7, 13, 59, 31, 19])


def read_input(filepath):
    with filepath.open() as fp:
        data = [line.strip() for line in fp if line.strip()]
    return int(data[0]), [int(x) for x in data[1].split(',') if x != 'x']


def get_waiting_time(arrive, bus_id):
    tmp = arrive // bus_id
    if tmp * bus_id == arrive:
        return 0
    tmp += 1
    return tmp * bus_id - arrive


def main():
    # arrive, bus_ids = TEST
    arrive, bus_ids = read_input(INPUT)
    waiting_times = []
    for bus_id in bus_ids:
        waiting_times.append((bus_id, get_waiting_time(arrive, bus_id)))
    waiting_times.sort(key=lambda x: x[1])
    bus = waiting_times[0]
    print(bus)
    print(bus[0] * bus[1])


if __name__ == '__main__':
    main()
