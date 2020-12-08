#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip().split('\n')


def read_input(filepath):
    with filepath.open() as fp:
        return [line.strip() for line in fp if line.strip()]

def main():
    # org_code = TEST
    org_code = read_input(INPUT)
    end = False
    count = 0
    for pos, line in enumerate(org_code):
        if end:
            break
        code = org_code[:]
        count += 1
        visited = set()
        pc = 0
        acc = 0
        if 'nop' in line:
            code[pos] = code[pos].replace('nop', 'jmp')
        elif 'jmp' in line:
            code[pos] = code[pos].replace('jmp', 'nop')
        while pc not in visited:
            visited.add(pc)
            try:
                cmd, param = code[pc].split(' ', 1)
            except IndexError:
                print(f'PROGRAM END, ACC: {acc}')
                end = True
                break
            param = int(param)
            if cmd == 'nop':
                pc += 1
            elif cmd == 'acc':
                acc += param
                pc += 1
            elif cmd == 'jmp':
                pc += param
    print(f'ACC: {acc}')
    print(f'Positions processed: {count}')


if __name__ == '__main__':
    main()
