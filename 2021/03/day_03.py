#!/usr/bin/python

from collections import defaultdict


def get_input():
    data = []
    with open('input_03.txt') as fp:
        for line in fp:
            if line.strip():
                data.append(line.strip())
    return data


def a():
    report = get_input()
    half = len(report) / 2
    bitwise = defaultdict(list)
    for code in report:
        for bit in range(len(code)):
            bitwise[bit].append(code[bit])
    gamma = []
    epsilon = []
    for i in range(len(bitwise)):
        sum_ = sum(map(int, bitwise[i]))
        if sum_ >= half:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    g = int(''.join(gamma), 2)
    e = int(''.join(epsilon), 2)
    print('gamma rate', ''.join(gamma), g)
    print('epsilon rate', ''.join(epsilon), e)
    print('Power consumption', g * e)
    return bitwise


def reduce_codes(codes, pos=0, keep_vals='10'):
    if len(codes) == 1:
        return codes[0]
    half = len(codes) / 2
    data = []
    for code in codes:
        data.append(code[pos])
    pos += 1
    sum_ = sum(map(int, data))
    if sum_ >= half:
        keep = keep_vals[0]
    else:
        keep = keep_vals[1]
    new_codes = [x for i, x in enumerate(codes) if data[i] == keep]
    return reduce_codes(new_codes, pos, keep_vals)


def b():
    report = get_input()
    oxy = reduce_codes(report)
    oxy_d = int(oxy, 2)
    print('Oxygen', oxy, oxy_d)
    co2 = reduce_codes(report, keep_vals='01')
    co2_d = int(co2, 2)
    print('CO2', co2, co2_d)
    print('Life support rating', oxy_d * co2_d)


def main():
    a()
    b()


if __name__ == '__main__':
    main()
