#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer
from queue import Empty


INPUT_FILE = 'input.txt'


def main(data):
    for system_id in (1, 5):
        ic = IntcodeComputer(data, init=system_id)
        ic.run()
        while True:
            try:
                print(ic.output)
            except Empty:
                break


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = fp.read()
    main(data)
