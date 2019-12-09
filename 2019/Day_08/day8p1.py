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
    count = WIDTH * HEIGHT
    idx = None
    for n, layer in enumerate(layers):
        count_0 = layer.count(0)
        if count_0 < count:
            count = count_0
            idx = n
    print(f'Layer {idx+1}:', count)
    layer = layers[idx]
    print(layer.count(1) * layer.count(2))


if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as fp:
        data = fp.read()
    main(data)
