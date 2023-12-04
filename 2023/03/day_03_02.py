import re

from collections import defaultdict
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'
GEAR_SYMBOL = '*'


class Symbol:
    RE = re.compile(r'[^0-9.]')

    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.symbol} ({self.x}, {self.y})'

    @classmethod
    def from_match(cls, match, x):
        return cls(match.group(0), x, match.start())


class PartNumber:
    RE = re.compile(r'\d+')

    def __init__(self, value, x, y_start, y_end):
        self.value = value
        self.x = x
        self.y_start = y_start
        self.y_end = y_end
        self.dx = set(range(x - 1, x + 2))
        self.dy = set(range(y_start - 1, y_end + 1))

    def __str__(self):
        return f'{self.value} ({self.x}, {self.y_start}-{self.y_end})'

    @classmethod
    def from_match(cls, match, x):
        value = int(match.group(0))
        return cls(value, x, match.start(), match.end())

    def is_adjacent(self, x, y):
        return (x in self.dx and y in self.dy)


def parse(data: str):
    numbers, symbols = [], []
    for x, line in enumerate(data.splitlines()):
        for m in Symbol.RE.finditer(line):
            symbols.append(Symbol.from_match(m, x))
        for m in PartNumber.RE.finditer(line):
            numbers.append(PartNumber.from_match(m, x))
    return numbers, symbols


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    numbers, symbols = parse(data)
    gears = defaultdict(list)
    for number in numbers:
        print(number, number.dx, number.dy)
        for symbol in symbols:
            if symbol.symbol != GEAR_SYMBOL:
                continue
            if number.is_adjacent(symbol.x, symbol.y):
                gears[(symbol.x, symbol.y)].append(number.value)
                break
    print(sum([x[0] * x[1] for x in gears.values() if len(x) == 2]))


if __name__ == '__main__':
    main()
