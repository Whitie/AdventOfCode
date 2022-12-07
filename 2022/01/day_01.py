from pathlib import Path


TEST = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

def get_input():
    with Path('input.txt').open() as fp:
        return fp.read()


def main():
    inp = get_input()
    calories = [sum(map(int, x.split('\n'))) for x in inp.strip().split('\n\n')]
    calories.sort(reverse=True)
    print('Part 1')
    print(calories[0])
    print('Part 2')
    print(sum(calories[:3]))


if __name__ == '__main__':
    main()
