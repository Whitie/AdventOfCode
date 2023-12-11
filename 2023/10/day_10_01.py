from collections import deque, namedtuple
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'

PIPES = {
    '|': ('n', 's'),
    '-': ('w', 'e'),
    'L': ('n', 'e'),
    'J': ('n', 'w'),
    '7': ('s', 'w'),
    'F': ('s', 'e'),
    'S': ('n', 's', 'w', 'e'),
}
DIRECTIONS = {
    'n': (-1, 0, 's'),
    's': (1, 0, 'n'),
    'w': (0, -1, 'e'),
    'e': (0, 1, 'w'),
}

Position = namedtuple('Position', 'x y')


def parse(data: str):
    return data.splitlines()


def get_start(map_: dict):
    for x, line in enumerate(map_):
        for y, c in enumerate(line):
            if c == 'S':
                return Position(x, y)


def _out_of_map(pos: Position, map_: dict):
    if (
        pos.x < 0 or
        pos.x > len(map_) or
        pos.y < 0 or
        pos.y > len(map_[pos.x])
    ):
        return True
    else:
        return False


def walk(start: Position, map_: dict):
    visited = {}
    search_path = deque([(start, 0)])
    while search_path:
        pos, distance = search_path.popleft()
        if pos not in visited:
            visited[pos] = distance
            possible = PIPES[map_[pos.x][pos.y]]
            for direction in possible:
                dx, dy, opposite = DIRECTIONS[direction]
                new_pos = Position(x=pos.x + dx, y=pos.y + dy)
                if not _out_of_map(new_pos, map_):
                    pipe = map_[new_pos.x][new_pos.y]
                    if pipe in PIPES:
                        directions = PIPES[pipe]
                        if opposite in directions:
                            search_path.append((new_pos, distance + 1))
    return visited


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    map_ = parse(data)
    start = get_start(map_)
    print(start)
    places = walk(start, map_)
    print(max(places.values()))


if __name__ == '__main__':
    main()
