#!/usr/bin/env python
# -*- coding: utf-8 -*-

INPUT_FILE = 'input.txt'
WIDTH = 25
HEIGHT = 6


def split_list(l, size):
    for i in range(0, len(l), size):
        yield l[i:i+size]


def _get_layers(data, width, height):
    return [x for x in split_list(data, width*height)]


def split_image_data(data, width, height):
    tmp = []
    for layer in _get_layers(data, width, height):
        tmp.append(split_list(layer, width))
    return tmp


def main(data):
    data = [int(x) for x in data.strip()]
    layers = _get_layers(data, WIDTH, HEIGHT)
    new = []
    for pixels in zip(*layers):
        for pixel in pixels:
            if pixel != 2:
                new.append(pixel)
                break
    for line in split_list(new, WIDTH):
        l = ''.join([str(x) for x in line])
        l = l.replace('0', ' ')
        print(l)


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = fp.read()
    main(data)
