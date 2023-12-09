from collections import namedtuple
from itertools import cycle
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'

Node = namedtuple('Node', 'left right')


def parse(data: str):
    instructions, raw_nodes = data.split('\n\n')
    nodes = {}
    for line in raw_nodes.splitlines():
        l, r = line.split('=')
        r1, r2 = r.strip(' ()').split(',')
        nodes[l.strip()] = Node(left=r1.strip(), right=r2.strip())
    return instructions, nodes


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    instructions, nodes = parse(data)
    current = 'AAA'
    for i, instruction in enumerate(cycle(instructions), start=1):
        if instruction == 'L':
            current = nodes[current].left
        else:
            current = nodes[current].right
        if current == 'ZZZ':
            print(i)
            break


if __name__ == '__main__':
    main()
