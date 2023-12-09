from collections import Counter
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'

CARDS = 'J23456789TQKA'


def get_card_values(hand):
    return tuple(CARDS.index(c) for c in hand)


def rate_hand(hand):
    values = sorted(Counter(hand).values())
    if (joker_count := hand.count('J')) and joker_count < 5:
        values.remove(joker_count)
        values[-1] += joker_count
    match values:
        case [5]:
            return 7
        case [1, 4]:
            return 6
        case [2, 3]:
            return 5
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 3
        case [1, 1, 1, 2]:
            return 2
        case [1, 1, 1, 1, 1]:
            return 1
        case _:
            raise ValueError(f'Unknown hand: {hand}')


def parse(data: str):
    deck = []
    for line in data.splitlines():
        cards, bid = line.split()
        deck.append((cards, int(bid)))
    return deck


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    deck = parse(data)
    result = []
    for cards, bid in deck:
        result.append((rate_hand(cards), get_card_values(cards), bid))
    print(sum((x+1) * bid for x, (_, _, bid) in enumerate(sorted(result))))


if __name__ == '__main__':
    main()
