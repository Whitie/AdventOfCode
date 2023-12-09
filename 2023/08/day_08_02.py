import math

from itertools import cycle
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse(data: str):
    instructions, raw_nodes = data.split('\n\n')
    nodes = {}
    for line in raw_nodes.splitlines():
        l, r = line.split('=')
        r1, r2 = r.strip(' ()').split(',')
        nodes[l.strip()] = r1.strip(), r2.strip()
    instructions = instructions.replace('L', '0').replace('R', '1')
    return list(map(int, instructions)), nodes


def find_z(node, nodes, instructions):
    for i, instruction in enumerate(cycle(instructions), start=1):
        next_node = nodes[node][instruction]
        node = next_node
        if node.endswith('Z'):
            return i


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    instructions, nodes = parse(data)
    currents = [x for x in nodes if x.endswith('A')]
    print(currents)
    steps = []
    for current in currents:
        steps.append(find_z(current, nodes, instructions))
    print(math.lcm(*steps))


if __name__ == '__main__':
    main()
