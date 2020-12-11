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
    directions = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    )
    count = 0
    for delta_y, delta_x in directions:
        ypos, xpos = y, x
        while True:
            ypos += delta_y
            xpos += delta_x
            if ypos < 0 or xpos < 0:
                break
            try:
                if area[ypos][xpos] in (OCCUPIED, EMPTY):
                    if area[ypos][xpos] == OCCUPIED:
                        count += 1
                    break
            except IndexError:
                break
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
                elif seat == OCCUPIED and occupied_count >= 5:
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
