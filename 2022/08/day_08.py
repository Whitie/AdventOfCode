from collections import defaultdict
from pathlib import Path


TEST = """\
30373
25512
65332
33549
35390
"""


def get_input():
    with Path('input.txt').open() as fp:
        return fp.read().rstrip()


def check_x(start, stop, y, tree, trees):
    visible = True
    for posx in range(start, stop):
        if trees[(posx, y)] >= tree:
            visible = False
    return visible


def check_y(start, stop, x, tree, trees):
    visible = True
    for posy in range(start, stop):
        if trees[(x, posy)] >= tree:
            visible = False
    return visible


def check(pos, trees):
    x, y = pos
    max_x, max_y = max(trees.keys())
    if x == 0 or y == 0 or x == max_x or y == max_y:
        return True
    tree = trees[pos]
    directions = []
    directions.append(check_x(0, x, y, tree, trees))
    directions.append(check_x(x + 1, max_x + 1, y, tree, trees))
    directions.append(check_y(0, y, x, tree, trees))
    directions.append(check_y(y + 1, max_y + 1, x, tree, trees))
    return any(directions)


def main():
    # inp = get_input()
    inp = TEST
    trees = defaultdict(int)
    for row, line in enumerate(inp.splitlines()):
        for column, tree in enumerate(line):
            trees[(column, row)] = int(tree)
    count = 0
    for pos, tree in trees.items():
        if check(pos, trees):
            count += 1
    print('Part 1')
    print(count)
    print('Part 2')


if __name__ == '__main__':
    main()
