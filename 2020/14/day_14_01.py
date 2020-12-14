#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
MEM_RE = re.compile(r'mem\[(?P<address>\d+)\]\s+=\s+(?P<value>\d+)', re.I)
TEST = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
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


def apply_mask(mask, value):
    result = []
    for m, v in zip(mask, bin(value)[2:].zfill(36)):
        if m == 'X':
            result.append(v)
        else:
            result.append(m)
    return int(''.join(result), 2)


def run_commands(memory, mask, commands):
    for address, value in commands:
        memory[address] = apply_mask(mask, value)
    return memory


def main():
    #program = parse_program(TEST)
    program = parse_program(read_input(INPUT))
    memory = {}
    for block in program:
        memory = run_commands(memory, **block)
    print(sum(memory.values()))


if __name__ == '__main__':
    main()
