#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


NUMBER_OF_CARDS = 10007


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
    new_deck = [None] * NUMBER_OF_CARDS
    pos = 0
    for card in deck:
        try:
            new_deck[pos] = card
            pos += inc
        except IndexError:
            pos -= NUMBER_OF_CARDS
            new_deck[pos] = card
            pos += inc
    return new_deck


def deal_into_new_stack(deck, *args):
    return deck[::-1]


def cut_cards(deck, cut):
    return deck[cut:] + deck[:cut]


def main(filename):
    commands = parse_input(filename)
    deck = list(range(NUMBER_OF_CARDS))
    dispatcher = {
        'inc': deal_with_increment,
        'new': deal_into_new_stack,
        'cut': cut_cards,
    }
    for command, arg in commands:
        deck = dispatcher[command](deck, arg)
    print(deck.index(2019))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
