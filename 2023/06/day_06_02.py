from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse(data: str):
    times, distances = data.split('\n')
    time = int(times.split(':')[1].replace(' ', ''))
    distance = int(distances.split(':')[1].replace(' ', ''))
    return time, distance


def first_win(race, reverse=False):
    time, distance = race
    times = range(time) if not reverse else reversed(range(time))
    for speed in times:
        if ((time - speed) * speed) > distance:
            return speed


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    races = [parse(data)]
    result = []
    for race in races:
        result.append((first_win(race), first_win(race, True)))
    result = [len(range(x, y+1)) for x, y in result]
    print(result)


if __name__ == '__main__':
    main()
