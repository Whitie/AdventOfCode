#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
OPTIONAL_FIELDS = {'cid'}

TEST = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


def read_input(filepath):
    with filepath.open() as fp:
        return fp.read().strip()


def parse_one_record(data):
    record = {}
    for pair in data.split():
        key, val = pair.split(':')
        record[key.strip()] = val.strip()
    return record


def parse_input(text):
    passports = []
    for data in text.split('\n\n'):
        data = data.replace('\n', ' ')
        passports.append(parse_one_record(data))
    return passports


def check_record(record):
    fields = set(record.keys())
    if fields >= REQUIRED_FIELDS:
        return True
    return False


def main():
    raw = read_input(INPUT)
    passports = parse_input(raw)
    valid = 0
    for passport in passports:
        if check_record(passport):
            valid += 1
    print(f'Valid: {valid}')


if __name__ == '__main__':
    main()
