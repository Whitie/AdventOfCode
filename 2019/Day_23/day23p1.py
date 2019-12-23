#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from queue import Empty, Queue
from threading import Thread

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


def main(filename):
    nodes = []
    queues = []
    for addr in range(50):
        queues.append((Queue(), Queue()))
        ic = IntcodeComputer.from_file(filename, queues[-1][0], queues[-1][1],
                                       addr)
        nodes.append(Thread(target=ic.run))
        nodes[-1].start()
    while True:
        for qin, qout in queues:
            try:
                out = qout.get_nowait()
                if out:
                    x = qout.get_nowait()
                    y = qout.get_nowait()
                    print(f'SEND TO {out}: X: {x}, Y: {y}')
                    if out == 255:
                        print(y)
                        break
                    queues[out][0].put_nowait(x)
                    queues[out][0].put_nowait(y)
            except Empty:
                qin.put_nowait(-1)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
