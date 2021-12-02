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


class RecursiveCombat:

    def __init__(self):
        self.player_1, self.player_2 = get_decks(TEST)
        # self.player_1, self.player_2 = get_decks(read_input(INPUT))

    def play(self, player_1, player_2):
        seen_1 = set()
        seen_2 = set()
        while player_1 and player_2:
            if tuple(player_1) in seen_1 and tuple(player_2) in seen_2:
                return 1
            else:
                seen_1.add(tuple(player_1))
                seen_2.add(tuple(player_2))
            p1, p2 = player_1.popleft(), player_2.popleft()
            if p1 <= len(player_1) and p2 <= len(player_2):
                winner = self.play(deque(list(player_1)[:p1]),
                                   deque(list(player_2)[:p2]))
            elif p1 > p2:
                winner = 1
                player_1.extend([p1, p2])
            else:
                winner = 2
                player_2.extend([p2, p1])
            return winner

    def main(self):
        winner = self.play(self.player_1, self.player_2)
        if winner == 1:
            print('Player 1 wins')
            print(sum(
                [x * y for x, y in enumerate(reversed(self.player_1), start=1)]
            ))
        else:
            print('Player 2 wins')
            print(sum(
                [x * y for x, y in enumerate(reversed(self.player_2), start=1)]
            ))


if __name__ == '__main__':
    RecursiveCombat().main()
