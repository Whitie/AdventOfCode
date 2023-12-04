from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse(data: str):
    points = []
    for card in data.splitlines():
        numbers = card.split(':')[1]
        winning, my = numbers.split('|')
        winning = set(winning.split())
        my = set(my.split())
        if (count := len(winning & my)):
            points.append(2**(count - 1))
    return points


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    numbers = parse(data)
    print(sum(numbers))


if __name__ == '__main__':
    main()
