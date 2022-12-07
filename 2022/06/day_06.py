from collections import deque
from pathlib import Path


TEST = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""


def get_input():
    with Path('input.txt').open() as fp:
        return fp.read().rstrip()


def get_marker_position(inp, marker_length):
    stack = deque(maxlen=marker_length)
    for pos, char in enumerate(inp, start=1):
        stack.append(char)
        if len(stack) == marker_length and len(set(stack)) == marker_length:
            return pos
    raise ValueError('No marker found')


def main():
    inp = get_input()
    # inp = TEST
    print('Part 1')
    print(get_marker_position(inp, 4))
    print('Part 2')
    print(get_marker_position(inp, 14))


if __name__ == '__main__':
    main()
