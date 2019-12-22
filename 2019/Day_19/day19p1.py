#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from queue import Empty

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


def main(filename):
    affected = 0
    for y in range(50):
        for x in range(50):
            ic = IntcodeComputer.from_file(filename)
            ic.in_queue.put(y)
            ic.in_queue.put(x)
            ic.run()
            try:
                out = ic.out_queue.get(timeout=0.5)
                affected += out
                print('#' if out else '.', end='')
            except Empty:
                pass
        print()
    print(affected)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
