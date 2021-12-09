#!/usr/bin/python

TEST = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | \
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | \
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | \
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | \
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | \
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | \
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | \
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | \
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | \
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | \
fgae cfgab fg bagce
"""
MAPPING = {
    2: '1',
    4: '4',
    3: '7',
    7: '8',
}


def get_input():
    data = []
    with open('input_08.txt') as fp:
        for line in fp:
            if line.strip():
                patterns, out = line.split('|', 1)
                data.append(
                    dict(input=patterns.strip().split(),
                         output=out.strip().split())
                )
    return data


def get_test_input():
    data = []
    for line in TEST.split('\n'):
        if line.strip():
            patterns, out = line.split('|', 1)
            data.append(
                dict(input=patterns.strip().split(),
                     output=out.strip().split())
            )
    return data


def a():
    digits = (2, 4, 3, 7)
    data = [x['output'] for x in get_input()]
    sum_ = 0
    for line in data:
        for num in line:
            if len(num) in digits:
                sum_ += 1
    print(sum_)


def b():
    data = [x['output'] for x in get_test_input()]
    for line in data:
        print('----------')
        for code in line:
            if len(code) in MAPPING:
                print(MAPPING[len(code)])
            else:
                print(code)


def main():
    a()
    b()


if __name__ == '__main__':
    main()
