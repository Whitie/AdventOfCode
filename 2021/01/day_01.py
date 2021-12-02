#!/usr/bin/python


def get_input():
    data = []
    with open('input_01.txt') as fp:
        for line in fp:
            if line.strip():
                data.append(int(line))
    return data


def get_chunks(it, n=3):
    chunks = []
    for i in range(len(it)):
        chunk = it[i:i+n]
        if len(chunk) != n:
            break
        chunks.append(chunk)
    return chunks


def a():
    data = get_input()
    inc = 0
    for i, val in enumerate(data[1:]):
        if val > data[i]:
            inc += 1
    print(inc)


def b():
    data = get_input()
    chunks = get_chunks(data)
    inc = 0
    for i, chunk in enumerate(chunks[1:]):
        if sum(chunk) > sum(chunks[i]):
            inc += 1
    print(inc)


def main():
    a()
    b()


if __name__ == '__main__':
    main()
