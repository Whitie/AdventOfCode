#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from functools import partial
from pathlib import Path


PATH = Path(__file__).parent.resolve()
INPUT = PATH / 'input.txt'
REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
OPTIONAL_FIELDS = {'cid'}

TEST = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


# Validators
def _between(first, last, val, _len=None):
    if _len and len(val) != _len:
        return False
    return first <= int(val) <= last


def _regex(pattern, val):
    if re.search(pattern, val):
        return True
    return False


def _validate_hgt(val):
    if val.endswith('cm'):
        return _between(150, 193, val.strip('cm'))
    elif val.endswith('in'):
        return _between(59, 76, val.strip('in'))
    else:
        return False


VALIDATORS = {
    'byr': partial(_between, first=1920, last=2002, _len=4),
    'iyr': partial(_between, first=2010, last=2020, _len=4),
    'eyr': partial(_between, first=2020, last=2030, _len=4),
    'hgt': _validate_hgt,
    'hcl': partial(_regex, pattern=r'^\#[0-9a-f]{6}$'),
    'ecl': partial(_regex, pattern=r'^(amb|blu|brn|gry|grn|hzl|oth)$'),
    'pid': partial(_regex, pattern=r'^\d{9}$'),
    'cid': lambda val: True,
}


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
        for field, val in record.items():
            if not VALIDATORS[field](val=val):
                print(f'Wrong: {field} {val}')
                return False
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
