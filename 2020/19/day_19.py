#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

from pathlib import Path


sys.setrecursionlimit(100000)

PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".strip().split('\n\n')


def read_input(filepath):
    with filepath.open() as fp:
        return fp.read().strip().split('\n\n')


def parse_rules(raw):
    rules = {}
    for line in raw.strip().split('\n'):
        num, rule = line.split(':')
        rules[num] = rule.strip().split()
    return rules


def solve(s, rules, d=0):
    if d > 1000:
        return ''
    if '"' in ''.join(s):
        return s[0].strip('"')
    else:
        regex = ['((']
        for char in s:
            if char == '|':
                regex.append(')|(')
            else:
                regex.append(solve(rules[char], rules, d + 1))
        regex.append('))')
        return ''.join(regex)


def main():
    # rules, data = TEST
    rules, data = read_input(INPUT)
    rules = parse_rules(rules)
    reg = re.compile('^{}$'.format(solve(rules['0'], rules)))
    count = 0
    for d in data.split('\n'):
        d = d.strip()
        m = reg.match(d)
        if m:
            count += 1
    print('Part 1:', count)
    rules['8'] = '42 | 42 8'.split()
    rules['11'] = '42 31 | 42 11 31'.split()
    reg = re.compile('^{}$'.format(solve(rules['0'], rules)))
    count = 0
    for d in data.split('\n'):
        d = d.strip()
        m = reg.match(d)
        if m:
            count += 1
    print('Part 2', count)


if __name__ == '__main__':
    main()
