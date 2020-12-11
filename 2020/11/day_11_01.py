#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
TEST = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip().split('\n')


def read_input(filepath):
    with filepath.open() as fp:
        return [list(line.strip()) for line in fp if line.strip()]


def get_occupied_count(y, x, area):
    positions = (
        (y-1, x-1), (y-1, x), (y-1, x+1),
        (y, x-1), (y, x+1),
        (y+1, x-1), (y+1, x), (y+1, x+1),
    )
    count = 0
    for ypos, xpos in positions:
        if ypos < 0 or xpos < 0:
            continue
        try:
            if area[ypos][xpos] == OCCUPIED:
                count += 1
        except IndexError:
            pass
    #for y, row in enumerate(area):
    #    for x, seat in enumerate(row):
    #        if seat == OCCUPIED and (y, x) in positions:
    #            count += 1
    return count


def main():
    #area = [list(row) for row in TEST]
    area = read_input(INPUT)
    rounds = 0
    while True:
        new_state = [[''] * len(area[0]) for _ in range(len(area))]
        for y, row in enumerate(area):
            for x, seat in enumerate(row):
                occupied_count = get_occupied_count(y, x, area)
                if seat == EMPTY and occupied_count == 0:
                    new_state[y][x] = OCCUPIED
                elif seat == OCCUPIED and occupied_count >= 4:
                    new_state[y][x] = EMPTY
                else:
                    new_state[y][x] = seat
        if area == new_state:
            break
        rounds += 1
        area = new_state
        #for row in new_state:
        #    print(''.join(row))
        #print()
    print(f'Rounds: {rounds}')
    print('Occupied:', sum([x.count(OCCUPIED) for x in area]))


if __name__ == '__main__':
    main()
