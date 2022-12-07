from collections import defaultdict, deque, namedtuple
from pathlib import Path


TEST = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
Move = namedtuple('Move', 'count from_stack to_stack')


def get_input():
    with Path('input.txt').open() as fp:
        return fp.read().rstrip()


def get_chunks(it, n, same_size=True):
    chunks = []
    for i in range(0, len(it), n):
        chunk = it[i:i+n]
        if len(chunk) != n and same_size:
            break
        chunks.append(chunk)
    return chunks


def parse_stacks(raw):
    stacks = defaultdict(deque)
    for line in list(reversed(raw.splitlines()))[1:]:
        for i, stack in enumerate(get_chunks(line, 4, False), start=1):
            if stack.strip():
                stacks[i].append(stack[1])
    return stacks


def parse_moves(raw):
    moves = []
    for line in raw.splitlines():
        if line.strip():
            parts = line.split()
            moves.append(
                Move(int(parts[1]), int(parts[3]), int(parts[5]))
            )
    return moves


def do_move(move, stacks):
    for _ in range(move.count):
        crate = stacks[move.from_stack].pop()
        stacks[move.to_stack].append(crate)
    return stacks


def do_moves(move, stacks):
    from_stack = list(stacks[move.from_stack])
    crates = from_stack[-move.count:]
    stacks[move.to_stack].extend(crates)
    stacks[move.from_stack] = deque(from_stack[:-move.count])
    return stacks


def main():
    inp = get_input()
    # inp = TEST
    raw_stacks, raw_moves = inp.split('\n\n')
    stacks = parse_stacks(raw_stacks)
    moves = parse_moves(raw_moves)
    for move in moves:
        stacks = do_move(move, stacks)
    print('Part 1')
    print(''.join([stacks[x][-1] for x in sorted(stacks.keys())]))
    print('Part 2')
    stacks = parse_stacks(raw_stacks)
    for move in moves:
        stacks = do_moves(move, stacks)
    print(''.join([stacks[x][-1] for x in sorted(stacks.keys())]))


if __name__ == '__main__':
    main()
