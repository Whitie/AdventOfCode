#!/usr/bin/python

from collections import defaultdict


TEST = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""
POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
POINTS_B = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
OPEN = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def get_input():
    with open('input_10.txt') as fp:
        return [x.strip() for x in fp if x.strip()]


def check_line(line):
    stack = []
    push = stack.append
    pop = stack.pop
    for char in line:
        if char in OPEN:
            push(char)
        else:
            last = pop()
            if char != OPEN[last]:
                print(f'Expected {OPEN[last]}, found {char}')
                return 'illegal', char
    if stack:
        return 'incomplete', stack
    else:
        return 'valid', None


def a():
    code = get_input()
    # code = TEST.strip().split('\n')
    parsed = defaultdict(list)
    points = 0
    for line in code:
        desc, char = check_line(line)
        parsed[desc].append(line)
        if isinstance(char, str):
            points += POINTS[char]
    print(points)


def calculate_line(line):
    sum_ = 0
    for char in line:
        sum_ *= 5
        sum_ += POINTS_B[char]
    return sum_


def b():
    code = get_input()
    # code = TEST.strip().split('\n')
    incomplete = []
    for line in code:
        desc, rest = check_line(line)
        if desc == 'incomplete':
            incomplete.append(''.join(OPEN[x] for x in reversed(rest)))
    print(incomplete)
    sums = []
    for line in incomplete:
        sums.append(calculate_line(line))
    sums.sort()
    print(sums[len(sums) // 2])


def main():
    a()
    b()


if __name__ == '__main__':
    main()
