from itertools import pairwise
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse(data: str):
    sequences = []
    for line in data.splitlines():
        sequences.append(map(int, line.split()))
    return sequences


def diff(seq):
    result = []
    for a, b in pairwise(seq):
        result.append(b - a)
    return result


def get_next(diffs):
    diffs.reverse()
    for i in range(len(diffs)):
        try:
            next_element = diffs[i][-1] + diffs[i+1][-1]
            diffs[i+1].append(next_element)
        except IndexError:
            break
    return next_element


def find_next_element(seq):
    diffs = [seq]
    while True:
        seq = diff(seq)
        diffs.append(seq)
        if not any(seq):
            break
    return get_next(diffs)


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    sequences = parse(data)
    next_elements = []
    for seq in sequences:
        next_elements.append(find_next_element(list(seq)))
    print(sum(next_elements))


if __name__ == '__main__':
    main()
