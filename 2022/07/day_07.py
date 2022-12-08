from collections import defaultdict
from pathlib import Path


TEST = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
TOTAL_SPACE = 70_000_000
TOTAL_NEEDED = 30_000_000


def get_input():
    with Path('input.txt').open() as fp:
        return fp.read().rstrip()


def parse_tree(inp):
    items = defaultdict(lambda: defaultdict(list))
    stack = []
    for line in inp.splitlines():
        if line.startswith('$'):
            _, command, *args = line.split()
            if command == 'cd':
                if args[0] == '..':
                    stack.pop()
                else:
                    stack.append(args[0])
        else:
            path = ''.join(stack)
            if line.startswith('dir'):
                _, name = line.split()
                items[path]['dirs'].append(path + name)
            else:
                size, name = line.split()
                items[path]['files'].append((int(size), name))
    return items


def sum_files(start, items, cache):
    sums = 0
    dirs = [start]
    while dirs:
        dir = dirs.pop()
        if dir in cache:
            sums += cache[dir]
        else:
            one_sum = sum([x[0] for x in items[dir]['files']])
            cache[dir] = one_sum
            sums += one_sum
        dirs.extend(items[dir]['dirs'])
    return sums, cache


def main():
    inp = get_input()
    # inp = TEST
    items = parse_tree(inp)
    print(len(items))
    sizes = {}
    cache = {}
    dirs = list(items.keys())
    for dir in dirs:
        size, cache = sum_files(dir, items, cache)
        sizes[dir] = size
    print('Part 1')
    print(sum([x for x in sizes.values() if x <= 100000]))
    print('Part 2')
    space_available = TOTAL_SPACE - sizes['/']
    needed = TOTAL_NEEDED - space_available
    candidates = {k: v for k, v in sizes.items() if v >= needed}
    print(min(candidates.values()))


if __name__ == '__main__':
    main()
