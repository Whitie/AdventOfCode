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


def get_ore(fuel, data):
    have = {k: 0 for k in data}
    need = {k: 0 for k in data}
    have['ORE'] = need['ORE'] = 0
    need['FUEL'] = fuel
    while fuel > 0:
        for chem in need:
            if chem == 'ORE' or need[chem] == 0:
                continue
            add = need[chem] - have[chem]
            if add > 0:
                r = ceil(add / data[chem][0])
                have[chem] += data[chem][0] * r
                for c, n in data[chem][1].items():
                    need[c] += n * r
                    if c != 'ORE':
                        fuel += n * r
            have[chem] -= need[chem]
            fuel -= need[chem]
            need[chem] = 0
    return need['ORE']


def main(filename):
    data = parse_input(filename)
    print('ORE:', get_ore(1, data))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <input_filename>')
