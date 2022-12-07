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
