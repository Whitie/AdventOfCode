from itertools import chain
from pathlib import Path
from time import monotonic

#
# Funktioniert nicht
#

INPUT = Path(__file__).parent.resolve() / 'input.txt'


class Mapping:

    def __init__(self, dest, source, range_):
        self.dest = dest
        self.source = source
        self.range_ = range_
        self.dest_range = range(dest, dest + range_)
        self.source_range = range(source, source + range_)

    def __repr__(self):
        return f'<Mapping({self.dest}, {self.source}, {self.range_})>'

    @classmethod
    def from_line(cls, line):
        return cls(*map(int, line.split()))

    def get_destination(self, source):
        try:
            return self.dest_range[self.source_range.index(source)]
        except ValueError:
            pass


def parse_mapping_block(block):
    return [Mapping.from_line(line) for line in block.splitlines()[1:]]


def parse(data: str):
    seeds_, *maps = data.split('\n\n')
    seeds_ = list(map(int, seeds_.split(':')[1].split()))
    seeds = []
    for i in range(0, len(seeds_), 2):
        seeds.append(range(seeds_[i], seeds_[i] + seeds_[i+1]))
    seeds = chain(*seeds)
    maps = [parse_mapping_block(x) for x in maps]
    return seeds, maps


def _process_mapping(mapping, source):
    for m in mapping:
        if (dest := m.get_destination(source)):
            return dest
    return source


def process_map(map_, sources):
    result = []
    for source in sources:
        result.append(_process_mapping(map_, source))
    return result


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    seeds, maps = parse(data)
    for i, map_ in enumerate(maps, start=1):
        print(f'Processing map {i}/{len(maps)}')
        start = monotonic()
        seeds = process_map(map_, seeds)
        print(f'Duration: {monotonic() - start:.1f}s')
    print(min(seeds))
    # print(maps)


if __name__ == '__main__':
    main()
