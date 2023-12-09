from pathlib import Path


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
    seeds, *maps = data.split('\n\n')
    seeds = map(int, seeds.split(':')[1].split())
    maps = [parse_mapping_block(x) for x in maps]
    return seeds, maps


def process_map(map_, sources):
    result = []
    for source in sources:
        result.append(source)
        for m in map_:
            if (dest := m.get_destination(source)):
                result[-1] = dest
                break
    return result


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    seeds, maps = parse(data)
    for map_ in maps:
        seeds = process_map(map_, seeds)
    print(min(seeds))
    # print(maps)


if __name__ == '__main__':
    main()
