from pathlib import Path


TEST = """\
A Y
B X
C Z
"""
TRANSLATE = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}


class Hand:
    
    def play(self, other):
        if self.name == other.name:
            points = 3
        elif other.name == self.beats:
            points = 6
        else:
            points = 0
        return points + self.points


class Rock(Hand):
    
    def __init__(self):
        self.name = 'Rock'
        self.points = 1
        self.beats = 'Scissors'


class Paper(Hand):
    
    def __init__(self):
        self.name = 'Paper'
        self.points = 2
        self.beats = 'Rock'


class Scissors(Hand):
    
    def __init__(self):
        self.name = 'Scissors'
        self.points = 3
        self.beats = 'Paper'


NAME_TO_OBJECT = {
    'Rock': Rock(),
    'Paper': Paper(),
    'Scissors': Scissors(),
}


def get_input():
    with Path('input.txt').open() as fp:
        return fp.read()


def main():
    hand_map = {
        'A': NAME_TO_OBJECT['Rock'],
        'B': NAME_TO_OBJECT['Paper'],
        'C': NAME_TO_OBJECT['Scissors'],
    }
    inp = get_input()
    # inp = TEST
    score = 0
    for game in inp.splitlines():
        player_code, me_code = game.strip().split(' ', 1)
        player = hand_map[player_code]
        me = hand_map[TRANSLATE[me_code]]
        # print(f'Me: {me.name} | Player: {player.name}')
        score += me.play(player)
    print('Part 1')
    print(f'Score: {score}')
    score = 0
    for game in inp.splitlines():
        player_code, result_code = game.strip().split(' ', 1)
        player = hand_map[player_code]
        if result_code == 'X':
            me = NAME_TO_OBJECT[player.beats]
        elif result_code == 'Y':
            me = NAME_TO_OBJECT[player.name]
        else:
            for hand in NAME_TO_OBJECT.values():
                if hand.beats == player.name:
                    me = hand
                    break
        print(f'Me: {me.name} | Player: {player.name}')
        score += me.play(player)
    print('Part 2')
    print(f'Score: {score}')

if __name__ == '__main__':
    main()
