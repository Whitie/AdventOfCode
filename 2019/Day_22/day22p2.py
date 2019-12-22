#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


LEN = 119315717514047
TIMES = 101741582076661


def parse_input(filename):
    commands = []
    with open(filename, 'r') as fp:
        for line in fp:
            if 'new' in line:
                commands.append(('new', None))
            elif 'increment' in line:
                num = int(line.split()[-1])
                commands.append(('inc', num))
            elif 'cut' in line:
                num = int(line.split()[-1])
                commands.append(('cut', num))
    return commands


def deal_with_increment(deck, inc):
    return ((deck[0] * inc) % LEN, (deck[1] * inc) % LEN)


def deal_into_new_stack(deck, *args):
    return ((-deck[0]) % LEN, (-deck[1] - 1) % LEN)


def cut_cards(deck, cut):
    return (deck[0], (deck[1] - cut) % LEN)


# copied from stackoverflow
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
# end stackoverflow part


def mod_pow(a, b, n):
    if b == 1:
        return a
    if b % 2 == 0:
        return mod_pow(a, b//2, n)**2 % n
    else:
        return a*mod_pow(a, b-1, n) % n


def main(filename):
    commands = parse_input(filename)
    deck = (1, 0)
    dispatcher = {
        'inc': deal_with_increment,
        'new': deal_into_new_stack,
        'cut': cut_cards,
    }
    for command, arg in commands:
        deck = dispatcher[command](deck, arg)
    a, b = deck
    an = mod_pow(a, TIMES, LEN)
    A, B = an, b * (an-1) * mod_inv(a-1, LEN)
    print((2020-B)*mod_inv(A, LEN) % LEN)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
