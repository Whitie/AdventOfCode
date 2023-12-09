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
    part_1, part_2 = [], []
    for sequence in sequences:
        seq = list(sequence)
        part_1.append(find_next_element(seq))
        seq.reverse()
        part_2.append(find_next_element(seq))
    print(f'Part 1: {sum(part_1)}')
    print(f'Part 2: {sum(part_2)}')


if __name__ == '__main__':
    main()
