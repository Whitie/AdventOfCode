#!/usr/bin/python

from functools import cache


def get_input(filename):
    with open(filename) as fp:
        data = fp.read().strip()
    return list(map(int, data.split(',')))


def a(days=80):
    fishs = get_input('input_06.txt')
    for day in range(days):
        add = 0
        for i in range(len(fishs)):
            if fishs[i] == 0:
                fishs[i] = 6
                add += 1
            else:
                fishs[i] -= 1
        fishs.extend([8] * add)
    print(len(fishs))


# Part B taken from Reddit:

@cache
def count_fish(life):
    if life < 0:
        return 1
    return count_fish(life - 7) + count_fish(life - 9)


def b():
    fishs = get_input('input_06.txt')
    print(sum(count_fish(255 - fish) for fish in fishs))


def main():
    a()
    b()


if __name__ == '__main__':
    main()
