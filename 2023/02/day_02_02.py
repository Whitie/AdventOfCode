import re

from collections import defaultdict
from math import prod
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'
COLORS = (
    ('red', 12),
    ('green', 13),
    ('blue', 14),
)


def check_line(line):
    _, line = line.split(':', 1)
    colors = defaultdict(int)
    for color, _ in COLORS:
        for m in re.finditer(rf'(\d+) ({color})', line):
            if int(m.group(1)) > colors[m.group(2)]:
                colors[m.group(2)] = int(m.group(1))
    return prod(colors.values())


def main():
    powers = []
    with INPUT.open() as fp:
        for line in fp:
            if line.strip():
                powers.append(check_line(line.strip()))
    print(sum(powers))


if __name__ == '__main__':
    main()
