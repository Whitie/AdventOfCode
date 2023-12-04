from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'
PAIRS = (
    ('zero', 'z0o'),
    ('one', 'o1e'),
    ('two', 't2o'),
    ('three', 't3e'),
    ('four', 'f4r'),
    ('five', 'f5e'),
    ('six', 's6x'),
    ('seven', 's7n'),
    ('eight', 'e8t'),
    ('nine', 'n9e'),
)


def parse_line(line):
    for word, subtitute in PAIRS:
        line = line.replace(word, subtitute)
    numbers = []
    for c in line:
        if c.isdigit():
            numbers.append(c)
    # print(numbers)
    return int(f'{numbers[0]}{numbers[-1]}')


def main():
    numbers = []
    with INPUT.open() as fp:
        for line in fp:
            if line.strip():
                numbers.append(parse_line(line.strip()))
    print(sum(numbers))


if __name__ == '__main__':
    main()
