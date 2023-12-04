from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse_line(line):
    numbers = []
    for c in line:
        if c.isdigit():
            numbers.append(c)
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
