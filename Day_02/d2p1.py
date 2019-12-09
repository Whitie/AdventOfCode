#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer


INPUT_FILE = 'input.txt'


def main(data):
    ic = IntcodeComputer(data)
    ic.code[1] = 12
    ic.code[2] = 2
    ic.run()
    print(ic.code[0])


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = fp.read()
    main(data)
