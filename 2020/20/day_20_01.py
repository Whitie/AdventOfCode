#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
TEST = PATH / 'test.txt'


class Tile:

    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.left = ''.join([x[0] for x in data])
        self.right = ''.join([x[-1] for x in data])
        self.top = data[0]
        self.bottom = data[-1]

    def __repr__(self):
        return f'Tile(id={self.id})'

    def __str__(self):
        return '\n'.join([f'Tile {self.id}:'] + self.data)


def read_input(filepath):
    tiles = []
    with filepath.open() as fp:
        for block in fp.read().strip().split('\n\n'):
            num, data = block.split('\n', 1)
            tile = Tile(int(num.strip('Tile: ')), data.strip().split('\n'))
            tiles.append(tile)
    return tiles


def get_matrix(count):
    width = height = math.sqrt(count)
    return [[0] * int(width) for _ in range(int(height))]


def find_corners(tiles):
    left = set([x.left for x in tiles])
    right = set([x.right for x in tiles])
    top = set([x.top for x in tiles])
    bottom = set([x.bottom for x in tiles])
    corners = []
    return corners


def main():
    tiles = read_input(TEST)
    # tiles = read_input(INPUT)
    sorted_tiles = get_matrix(len(tiles))
    print(sorted_tiles)
    corners = find_corners(tiles)
    print(corners)


if __name__ == '__main__':
    main()
