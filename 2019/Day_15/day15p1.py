#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from collections import defaultdict
from threading import Thread

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


INPUT_FILE = 'input.txt'
MOVES = ['#', '.', 'O']


def main(filename):
    ic = IntcodeComputer.from_file(filename)
    robot = Thread(target=ic.run)
    robot.start()
    loc = defaultdict(int)
    start = [0, 0]
    while True:
        cmd = int(input('CMD: '))
        if cmd == 0:
            break
        ic.in_queue.put(cmd)
        out = ic.out_queue.get()
        if out == 2:
            break
        start[0] += 1
    print(start)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
