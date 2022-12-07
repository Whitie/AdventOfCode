from itertools import count
from pathlib import Path
from string import ascii_letters


TEST = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
POINTS = dict(zip(ascii_letters, count(start=1)))


def get_input():
    with Path('input.txt').open() as fp:
        return fp.read().strip()


def get_chunks(it, n=3):
    chunks = []
    for i in range(0, len(it), n):
        chunk = it[i:i+n]
        if len(chunk) != n:
            break
        chunks.append(chunk)
    return chunks


def main():
    inp = get_input()
    # inp = TEST
    priority = 0
    for rucksack in inp.splitlines():
        half = len(rucksack) // 2
        comp_1 = set(rucksack[:half])
        comp_2 = set(rucksack[half:])
        items = comp_1 & comp_2
        assert len(items) == 1
        item = list(items)[0]
        priority += POINTS[item]
    print('Part 1')
    print(priority)
    priority = 0
    for r1, r2, r3 in get_chunks(inp.splitlines()):
        r1, r2, r3 = set(r1), set(r2), set(r3)
        items = r1 & r2 & r3
        assert len(items) == 1
        item = list(items)[0]
        priority += POINTS[item]
    print('Part 2')
    print(priority)


if __name__ == '__main__':
    main()
