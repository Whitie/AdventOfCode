from collections import defaultdict
from itertools import combinations
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse(data: str):
    map_ = []
    for line in data.splitlines():
        map_.append([x == '#' for x in line])
    return map_


def find_empty_space(map_: list[list[bool]]):
    cols_map = defaultdict(int)
    rows = []
    for i, row in enumerate(map_):
        if not any(row):
            rows.append(i)
        for j, col in enumerate(row):
            if not col:
                cols_map[j] += 1
    cols = [x for x, y in cols_map.items() if y == len(map_)]
    cols.sort()
    return cols, rows


def expand(cols: list, rows: list, map_: list):
    for offset, row in enumerate(rows):
        map_.insert(row + offset, [False for _ in range(len(map_[0]))])
    for offset, col in enumerate(cols):
        for i in range(len(map_)):
            map_[i].insert(col + offset, False)
    return map_


def caculate_distances(galaxies: dict):
    distances = []
    for gal_1, gal_2 in combinations(galaxies.keys(), 2):
        x1, y1 = galaxies[gal_1]
        x2, y2 = galaxies[gal_2]
        distances.append(abs(x1 - x2) + abs(y1 - y2))
    return distances


def substitute_and_count(map_: list[list[bool]]):
    count = 1
    galaxies = {}
    for i, row in enumerate(map_):
        for j, col in enumerate(row):
            if col:
                map_[i][j] = count
                galaxies[count] = i, j
                count += 1
    return galaxies, map_


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    map_ = parse(data)
    empty_cols, empty_rows = find_empty_space(map_)
    map_ = expand(empty_cols, empty_rows, map_)
    galaxies, map_ = substitute_and_count(map_)
    print(galaxies)
    distances = caculate_distances(galaxies)
    print(sum(distances))


if __name__ == '__main__':
    main()
