#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer
from itertools import permutations
from queue import LifoQueue
from threading import Thread


INPUT_FILE = 'input.txt'


def main(data):
    powers = []
    for perm in permutations(range(5, 10)):
        a_in = LifoQueue()
        a_b = LifoQueue()
        b_c = LifoQueue()
        c_d = LifoQueue()
        d_e = LifoQueue()
        out = LifoQueue()
        a_in.put(0)
        a = IntcodeComputer(data, in_queue=a_in, out_queue=a_b, init=perm[0])
        t1 = Thread(target=a.run)
        t1.start()
        b = IntcodeComputer(data, in_queue=a_b, out_queue=b_c, init=perm[1])
        t2 = Thread(target=b.run)
        t2.start()
        c = IntcodeComputer(data, in_queue=b_c, out_queue=c_d, init=perm[2])
        t3 = Thread(target=c.run)
        t3.start()
        d = IntcodeComputer(data, in_queue=c_d, out_queue=d_e, init=perm[3])
        t4 = Thread(target=d.run)
        t4.start()
        e = IntcodeComputer(data, in_queue=d_e, out_queue=out, init=perm[4])
        t5 = Thread(target=e.run)
        t5.start()
        while True:
            result = out.get()
            if e.halt:
                powers.append(result)
                break
            else:
                a_in.put(result)
    print(max(powers))


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = fp.read()
    main(data)
