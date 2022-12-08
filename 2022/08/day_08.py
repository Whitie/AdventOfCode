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


def main():
    # inp = get_input()
    inp = TEST
    trees = []
    for line in inp.splitlines():
        trees.append(list(map(int, line)))
    count = (len(trees) - 2) * 2 + len(trees[0]) * 2
    print('Part 1')
    print(count)
    print('Part 2')


if __name__ == '__main__':
    main()
