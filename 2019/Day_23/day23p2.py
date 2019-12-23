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
    nat = None
    idle = False
    last = None
    while True:
        if idle and nat:
            x, y = nat
            queues[0][0].put_nowait(x)
            queues[0][0].put_nowait(y)
            print('NAT sending', x, y)
            if y == last:
                print('TWICE in a row:', y)
                break
            last = y
        idle = False
        sendout = []
        for qin, qout in queues:
            try:
                out = qout.get_nowait()
                if out:
                    x = qout.get_nowait()
                    y = qout.get_nowait()
                    print(f'SEND TO {out}: X: {x}, Y: {y}')
                    if out == 255:
                        nat = x, y
                    else:
                        queues[out][0].put_nowait(x)
                        queues[out][0].put_nowait(y)
                        sendout.append(out)
            except Empty:
                pass
            for q in [x for x in range(50) if x not in sendout]:
                queues[q][0].put_nowait(-1)
            if not sendout:
                idle = True


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
