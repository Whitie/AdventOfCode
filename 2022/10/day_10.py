from pathlib import Path


TEST = """\
"""


def get_input(filename='input.txt'):
    with Path(filename).open() as fp:
        return fp.read().rstrip()


def parse_instruction(inp):
    for line in inp.splitlines():
        inst, *arg = line.split()
        if arg:
            yield inst, int(arg[0])
        else:
            yield inst, None


def main():
    # inp = get_input()
    inp = get_input('test.txt')
    cycles = 1
    collect = 20
    x = 1
    instructions = iter(parse_instruction(inp))
    while True:
        try:
            instruction, arg = next(instructions)
        except StopIteration:
            break
        if instruction == 'noop':
            cycles += 1
        elif instruction == 'addx':
            cycles += 2
        if cycles >= collect:
            print(x * collect)
            collect += 40
            if collect == 220:
                break
        if instruction == 'addx':
            x += arg
    print('Part 1')
    print('Part 2')


if __name__ == '__main__':
    main()
