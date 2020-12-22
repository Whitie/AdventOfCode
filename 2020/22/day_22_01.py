#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip()


def read_input(filepath):
    with filepath.open() as fp:
        return fp.read().strip()


def get_decks(raw):
    p1, p2 = raw.split('\n\n', 1)
    player_1 = deque(int(x) for x in p1.splitlines()[1:])
    player_2 = deque(int(x) for x in p2.splitlines()[1:])
    return player_1, player_2


def main():
    # player_1, player_2 = get_decks(TEST)
    player_1, player_2 = get_decks(read_input(INPUT))
    rounds = 0
    while True:
        rounds += 1
        p1, p2 = player_1.popleft(), player_2.popleft()
        if p1 > p2:
            player_1.extend([p1, p2])
        else:
            player_2.extend([p2, p1])
        if not player_1 or not player_2:
            break
    print(f'Rounds: {rounds}')
    if player_1:
        print('Player 1 wins')
        print(sum([x * y for x, y in enumerate(reversed(player_1), start=1)]))
    else:
        print('Player 2 wins')
        print(sum([x * y for x, y in enumerate(reversed(player_2), start=1)]))


if __name__ == '__main__':
    main()
