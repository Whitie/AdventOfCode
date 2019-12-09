#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer


INPUT_FILE = 'input.txt'
OUTPUT = 19690720


def main(data):
    for i in range(100):
        for j in range(100):
            ic = IntcodeComputer(data)
            ic.code[1] = i
            ic.code[2] = j
            ic.run()
            if ic.code[0] == OUTPUT:
                return i, j


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = fp.read()
    noun, verb = main(data)
    print(noun, verb)
    print(100 * noun + verb)
