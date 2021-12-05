#!/usr/bin/python


TEST = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class BingoNumber:

    def __init__(self, number):
        self.number = number
        self.marked = False

    def __bool__(self):
        return self.marked

    def __eq__(self, other):
        return self.number == other


class Bingo:

    def __init__(self, fields):
        self.fields = fields
        self.last = None
        self.winner = False
        self.cols = []
        for line in fields:
            for i, num in enumerate(line):
                try:
                    self.cols[i].append(num)
                except IndexError:
                    self.cols.append([num])

    @classmethod
    def from_string(cls, s):
        lines = s.split('\n')
        fields = []
        for line in lines:
            if line.strip():
                fields.append([BingoNumber(int(x)) for x in line.split()])
        return cls(fields)

    def mark(self, number):
        self.last = number
        for line in self.fields:
            for num in line:
                if num == number:
                    num.marked = True

    def wins(self):
        for line in self.fields:
            if all([bool(x) for x in line]):
                self.winner = True
                return True
        for col in self.cols:
            if all([bool(x) for x in col]):
                self.winner = True
                return True
        return False

    def score(self):
        sum_ = 0
        for line in self.fields:
            for num in line:
                if not num.marked:
                    sum_ += num.number
        return sum_ * self.last


def get_input():
    with open('input_04.txt') as fp:
        return fp.read()


def play(bingos, numbers):
    for number in numbers:
        for bingo in bingos:
            bingo.mark(number)
            if bingo.wins():
                print('WIN')
                return bingo


def play_b(bingos, numbers):
    while True:
        for number in numbers:
            for bingo in bingos:
                bingo.mark(number)
                bingo.wins()
                if all([x.winner for x in bingos]):
                    print('Last Found')
                    return bingo


def a():
    # raw = TEST
    raw = get_input()
    splitted = raw.split('\n\n')
    numbers = map(int, splitted[0].split(','))
    bingos = [Bingo.from_string(x) for x in splitted[1:]]
    winner = play(bingos, numbers)
    print(winner.score())


def b():
    # raw = TEST
    raw = get_input()
    splitted = raw.split('\n\n')
    numbers = map(int, splitted[0].split(','))
    bingos = [Bingo.from_string(x) for x in splitted[1:]]
    last_winner = play_b(bingos, numbers)
    print(last_winner.score())


def main():
    a()
    b()


if __name__ == '__main__':
    main()
