#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from queue import Empty

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402

SCRIPT = [
    'NOT A J',
    'NOT J J',
    'AND B J',
    'AND C J',
    'NOT J J',
    'AND D J',
    'WALK'
]


def main(filename):
    ic = IntcodeComputer.from_file(filename)
    for line in reversed(SCRIPT):
        [ic.in_queue.put(ord(x)) for x in reversed(line+'\n')]
    ic.run()
    out = []
    while True:
        try:
            out.append(ic.output)
        except Empty:
            break
    try:
        print(''.join([chr(x) for x in reversed(out)]))
    except ValueError:
        print('DAMAGE:', out[0])


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
