#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from collections import defaultdict

sys.path.insert(0, os.path.abspath('..'))

from utils import Point  # noqa: E402


class Eris:

    def __init__(self, map):
        self.map = map
        self.maps = []
        self.seen = False
        self.save_map(map)

    @classmethod
    def from_file(cls, filename):
        map_ = defaultdict(int)
        with open(filename, 'r') as fp:
            for y, line in enumerate(fp):
                for x, cell in enumerate(line.strip()):
                    if cell == '#':
                        map_[Point(x, y)] = 1
        return cls(map_)

    def get_neighbor_bugs(self, point):
        neighbors = 0
        for p in point.neighbors:
            if p in self.map:
                neighbors += self.map[p]
        return neighbors

    def next_state(self):
        new_map = defaultdict(int)
        for y in range(5):
            for x in range(5):
                point = Point(x, y)
                bugs = self.get_neighbor_bugs(point)
                if self.map[point] and bugs == 1:
                    new_map[point] = 1
                elif not self.map[point] and bugs in (1, 2):
                    new_map[point] = 1
        self.save_map(new_map)
        return new_map

    def biodiversity_rating(self, points):
        num = 0
        bio = 0
        for y in range(5):
            for x in range(5):
                if Point(x, y) in points:
                    bio += 2**num
                num += 1
        return bio

    def save_map(self, map):
        to_save = set([k for k, v in map.items() if v])
        if to_save in self.maps:
            print('Map already seen')
            print(self.biodiversity_rating(to_save))
            self.seen = True
        else:
            self.maps.append(to_save)

    def run(self, rounds=None):
        if rounds is None:
            while not self.seen:
                next_map = self.next_state()
                self.map = next_map
        else:
            for _ in range(rounds):
                next_map = self.next_state()
                self.map = next_map


def main(filename):
    eris = Eris.from_file(filename)
    eris.run()


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
