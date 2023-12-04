from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


class Card:

    def __init__(self, winning, my_set):
        self.winning = winning
        self.my_set = my_set
        self.count = 1

    @classmethod
    def from_line(cls, line):
        numbers = line.split(':')[1]
        winning, my = numbers.split('|')
        return cls(set(winning.split()), set(my.split()))

    @property
    def win_count(self):
        return len(self.winning & self.my_set)


def parse(data: str):
    cards = []
    for line in data.splitlines():
        cards.append(Card.from_line(line))
    for i in range(len(cards)):
        if (win_count := cards[i].win_count):
            for j in range(i + 1, i + 1 + win_count):
                cards[j].count += cards[i].count
    return cards


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    numbers = parse(data)
    print(sum([x.count for x in numbers]))


if __name__ == '__main__':
    main()
