#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

from itertools import combinations
from math import gcd


MOONS = ('Io', 'Europa', 'Ganymede', 'Callisto')
POS_RE = re.compile(r'<x=(-?\d+).+?y=(-?\d+).+?z=(-?\d+)>')


class Position:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_string(cls, s):
        match = POS_RE.search(s)
        if match:
            x, y, z = map(int, match.groups())
            return cls(x, y, z)

    def __str__(self):
        return f'<x={self.x}, y={self.y}, z={self.z}>'


class Velocity(Position):
    pass


class Moon:

    def __init__(self, name, position, velocity=None):
        self.name = name
        self.position = position
        self.velocity = velocity or Velocity()

    def update_position(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    @property
    def potential_energy(self):
        return (abs(self.position.x) + abs(self.position.y)
                + abs(self.position.z))

    @property
    def kinetic_energy(self):
        return (abs(self.velocity.x) + abs(self.velocity.y)
                + abs(self.velocity.z))

    @property
    def energy(self):
        return self.potential_energy * self.kinetic_energy

    def __str__(self):
        return f'{self.name:<10} pos={self.position}, vel={self.velocity}'

    __repr__ = __str__


def read_input(filename):
    with open(filename, 'r') as fp:
        data = [line.strip() for line in fp if line.strip()]
    assert len(data) == 4
    moons = []
    for name, pos in zip(MOONS, data):
        position = Position.from_string(pos)
        moons.append(Moon(name, position))
    return moons


def apply_gravity(moon_1, moon_2):
    if moon_1.position.x > moon_2.position.x:
        moon_1.velocity.x -= 1
        moon_2.velocity.x += 1
    elif moon_1.position.x < moon_2.position.x:
        moon_1.velocity.x += 1
        moon_2.velocity.x -= 1
    if moon_1.position.y > moon_2.position.y:
        moon_1.velocity.y -= 1
        moon_2.velocity.y += 1
    elif moon_1.position.y < moon_2.position.y:
        moon_1.velocity.y += 1
        moon_2.velocity.y -= 1
    if moon_1.position.z > moon_2.position.z:
        moon_1.velocity.z -= 1
        moon_2.velocity.z += 1
    elif moon_1.position.z < moon_2.position.z:
        moon_1.velocity.z += 1
        moon_2.velocity.z -= 1


def simulate(moons):
    for moon_1, moon_2 in combinations(moons, 2):
        apply_gravity(moon_1, moon_2)
    for moon in moons:
        moon.update_position()
    return moons


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main(filename):
    moons = read_input(filename)
    steps = 0
    periods = [0, 0, 0]
    start = {
        'x': ([x.position.x for x in moons], [x.velocity.x for x in moons]),
        'y': ([x.position.y for x in moons], [x.velocity.y for x in moons]),
        'z': ([x.position.z for x in moons], [x.velocity.z for x in moons]),
    }
    while True:
        moons = simulate(moons)
        steps += 1
        if (
            [x.position.x for x in moons] == start['x'][0]
            and [x.velocity.x for x in moons] == start['x'][1]
            and not periods[0]
        ):
            periods[0] = steps
        if (
            [x.position.y for x in moons] == start['y'][0]
            and [x.velocity.y for x in moons] == start['y'][1]
            and not periods[1]
        ):
            periods[1] = steps
        if (
            [x.position.z for x in moons] == start['z'][0]
            and [x.velocity.z for x in moons] == start['z'][1]
            and not periods[2]
        ):
            periods[2] = steps
        if all(periods):
            break
        if steps % 1000 == 0:
            print(steps)
    print(f'Steps: {periods}')
    print('Pos:', lcm(lcm(periods[0], periods[1]), periods[2]))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
