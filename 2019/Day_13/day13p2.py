#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from intcode import IntcodeComputer  # noqa: E402


INPUT_FILE = 'input.txt'


def main(filename):
    ic = IntcodeComputer.from_file(filename)
    offset = 639
    height = ic.code[604]
    width = max(ic.code[620], ic.code[621]) // height
    no = ic.code[632]
    a = max(ic.code[612], ic.code[613])
    b = max(ic.code[616], ic.code[617])
    s = 0
    for y in range(height):
        for x in range(width):
            if ic.code[offset+y*width+x] == 2:
                s += ic.code[no+(((x*height+y)*a+b) % (width*height))]
    print(s)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
