#!/usr/bin/python

# 19 paths
TEST = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""
INPUT = """\
mx-IQ
mx-HO
xq-start
start-HO
IE-qc
HO-end
oz-xq
HO-ni
ni-oz
ni-MU
sa-IE
IE-ni
end-sa
oz-sa
MU-start
MU-sa
oz-IE
HO-xq
MU-xq
IE-end
MU-mx
"""


def get_input(inp=TEST):
    data = []
    for line in inp.strip().split('\n'):
        a, b = line.split('-')
        if b == 'start' or a == 'end':
            a, b = b, a
        data.append((a, b))
    return data


def a():
    data = get_input()
    starts = [x for x in data if x[0] == 'start']
    print(starts)


def b():
    pass


def main():
    a()
    b()


if __name__ == '__main__':
    main()
