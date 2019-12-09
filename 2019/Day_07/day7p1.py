#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer
from itertools import permutations
from queue import LifoQueue


INPUT_FILE = 'input.txt'


def main(data):
    powers = []
    for perm in permutations(range(5)):
        q = LifoQueue()
        q.put(0)
        for phase in perm:
            ic = IntcodeComputer(data, in_queue=q, out_queue=q)
            q.put(phase)
            ic.run()
        powers.append(q.get())
    print(max(powers))


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = fp.read()
    main(data)
