from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse(data: str):
    return [x.strip() for x in data.split(',')]


def _hash(code: str):
    current = 0
    for c in code:
        current += ord(c)
        current *= 17
        current %= 256
    return current


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    codes = parse(data)
    hashes = []
    for code in codes:
        hashes.append(_hash(code))
    print(sum(hashes))


if __name__ == '__main__':
    main()