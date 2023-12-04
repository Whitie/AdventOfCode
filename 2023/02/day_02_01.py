import re

from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'
COLORS = (
    ('red', 12),
    ('green', 13),
    ('blue', 14),
)


def check_line(line):
    game, line = line.split(':', 1)
    for color, max in COLORS:
        for m in re.finditer(rf'(\d+) {color}', line):
            if int(m.group(1)) > max:
                return 0
    return int(game.split()[-1])


def main():
    ids = []
    with INPUT.open() as fp:
        for line in fp:
            if line.strip():
                ids.append(check_line(line.strip()))
    print(sum(ids))


if __name__ == '__main__':
    main()
