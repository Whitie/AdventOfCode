from pathlib import Path


TEST = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def get_input():
    with Path('input.txt').open() as fp:
        return fp.read().strip()


def parse_sections(raw):
    tmp = []
    for section in raw.split(',', 1):
        start, end = section.split('-', 1)
        tmp.append(set(range(int(start), int(end) + 1)))
    assert len(tmp) == 2
    return tmp[0], tmp[1]


def main():
    inp = get_input()
    # inp = TEST
    count_fully = 0
    count_overlap = 0
    for sections in inp.splitlines():
        sec_1, sec_2 = parse_sections(sections)
        if sec_1.issubset(sec_2) or sec_1.issuperset(sec_2):
            count_fully += 1
        if len(sec_1 & sec_2):
            count_overlap += 1
    print('Part 1')
    print(count_fully)
    print('Part 2')
    print(count_overlap)


if __name__ == '__main__':
    main()
