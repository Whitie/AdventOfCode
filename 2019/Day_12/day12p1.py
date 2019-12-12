#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

from itertools import combinations


MOONS = ('Io', 'Europa', 'Ganymede', 'Callisto')
STEPS = 1000
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


def main(filename):
    moons = read_input(filename)
    for i in range(STEPS):
        for moon_1, moon_2 in combinations(moons, 2):
            apply_gravity(moon_1, moon_2)
        for moon in moons:
            moon.update_position()
    energy = 0
    for moon in moons:
        print(f'{moon} | E: {moon.energy}')
        energy += moon.energy
    print(f'Total energy: {energy}')


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print(f'Usage: {sys.argv[0]} <filename>')
