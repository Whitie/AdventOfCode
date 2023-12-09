from math import prod
from pathlib import Path


INPUT = Path(__file__).parent.resolve() / 'input.txt'


def parse(data: str):
    times, distances = data.split('\n')
    times = map(int, times.split(':')[1].split())
    distances = map(int, distances.split(':')[1].split())
    return zip(times, distances)


def first_win(race, reverse=False):
    time, distance = race
    times = range(time) if not reverse else reversed(range(time))
    for speed in times:
        if ((time - speed) * speed) > distance:
            return speed


def main():
    with INPUT.open() as fp:
        data = fp.read().strip()
    races = parse(data)
    result = []
    for race in races:
        result.append((first_win(race), first_win(race, True)))
    result = [len(range(x, y+1)) for x, y in result]
    print(result)
    print(prod(result))


if __name__ == '__main__':
    main()
