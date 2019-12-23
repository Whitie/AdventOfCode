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


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
