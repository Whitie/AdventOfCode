from pathlib import Path


TEST = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
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
