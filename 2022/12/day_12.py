from pathlib import Path


TEST = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def get_input():
    with Path('input.txt').open() as fp:
        return fp.read().rstrip()


def main():
    # inp = get_input()
    inp = TEST
    print('Part 1')
    print('Part 2')


if __name__ == '__main__':
    main()
