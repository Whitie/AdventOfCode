#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from collections import defaultdict
from math import ceil


def parse_chemical(chem):
    amount, chemical = chem.split()
    return chemical.strip(), int(amount.strip())


def parse_input(filename):
    data = {}
    with open(filename, 'r') as fp:
        for line in fp:
            if line.strip():
                source, chemical = line.split('=>')
                out, units = parse_chemical(chemical)
                sources = dict(parse_chemical(x) for x in source.split(','))
                data[out] = (units, sources)
    return data


def main(filename):
    data = parse_input(filename)
    print(data)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <input_filename>')
