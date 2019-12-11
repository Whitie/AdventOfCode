#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def get_input(filename):
    inp = []
    with open(filename, 'r') as fp:
        for line in fp:
            line = line.strip()
            if line:
                inp.append(line)
    return inp


def diff(check, line):
    tmp = []
    for pos, pair in enumerate(zip(check, line)):
        if pair[0] != pair[1]:
            tmp.append((pos, pair[0]))
    return tmp


def check_line(pos, lines):
    check = lines[pos]
    for line in lines[pos+1:]:
        diff_chars = diff(check, line)
        if len(diff_chars) == 1:
            print(diff_chars[0])
            pos = diff_chars[0][0]
            return check[:pos] + check[pos+1:]


def main(filename):
    inp = get_input(filename)
    for pos in range(len(inp)):
        common = check_line(pos, inp)
        if common is not None:
            break
    print(''.join(common))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
