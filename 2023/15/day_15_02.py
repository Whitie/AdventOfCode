from collections import defaultdict
from functools import partial
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse(data: str):
    return [x.strip() for x in data.split(',')]


def _hash(code: str):
    current = 0
    for c in code:
        current += ord(c)
        current *= 17
        current %= 256
    return current


def _find_index(label, box):
    index = None
    for i, lens in enumerate(box):
        if lens[0] == label:
            index = i
            break
    return index


def _remove_lens(box_num, boxes, label):
    index = _find_index(label, boxes[box_num])
    if index is not None:
        boxes[box_num].pop(index)
    return boxes


def _add_lens(box_num, boxes, label, focal_length):
    index = _find_index(label, boxes[box_num])
    if index is None:
        boxes[box_num].append((label, focal_length))
    else:
        boxes[box_num][index] = (label, focal_length)
    return boxes


def parse_code(code: str):
    if '=' in code:
        label, focal_length = code.split('=')
        operation = partial(
            _add_lens, label=label, focal_length=int(focal_length)
        )
    else:
        label = code.strip('-')
        operation = partial(_remove_lens, label=label)
    return label, operation


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    codes = parse(data)
    boxes = defaultdict(list)
    for code in codes:
        label, operation = parse_code(code)
        box_num = _hash(label)
        boxes = operation(box_num, boxes)
    power = 0
    for box_num, lenses in boxes.items():
        for slot, lens in enumerate(lenses, start=1):
            power += (box_num + 1) * slot * lens[1]
    print(power)


if __name__ == '__main__':
    main()
