#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from itertools import product
from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
MEM_RE = re.compile(r'mem\[(?P<address>\d+)\]\s+=\s+(?P<value>\d+)', re.I)
TEST = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip().split('\n')


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]


def parse_program(lines):
    parsed = []
    for line in lines:
        if line.startswith('mask'):
            _, mask = line.split('=')
            parsed.append(dict(mask=mask.strip(), commands=[]))
        else:
            match = MEM_RE.search(line)
            if match:
                parsed[-1]['commands'].append(
                    (int(match.group('address')), int(match.group('value')))
                )
    return parsed


def apply_mask(mask, address):
    result = []
    for m, v in zip(mask, bin(address)[2:].zfill(36)):
        if m == '0':
            result.append(v)
        else:
            result.append(m)
    mask = ''.join(result)
    addresses = []
    for combination in product('01', repeat=mask.count('X')):
        addr = mask[:]
        for num in combination:
            addr = addr.replace('X', num, 1)
        addresses.append(int(addr, 2))
    return addresses


def run_commands(memory, mask, commands):
    for address, value in commands:
        addresses = apply_mask(mask, address)
        for addr in addresses:
            memory[addr] = value
    return memory


def main():
    # program = parse_program(TEST)
    program = parse_program(read_input(INPUT))
    memory = {}
    for block in program:
        memory = run_commands(memory, **block)
    print(sum(memory.values()))


if __name__ == '__main__':
    main()
