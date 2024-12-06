DAY = 0
FILENAME = 'test.txt'
PATH = f'data/day{DAY}/{FILENAME}'


def read_input(filename: str) -> list[int]:
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def part1(data: list[int]) -> int:
    return 0


def part2(data: list[int]) -> int:
    return 0


def main():
    data = read_input(PATH)
    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()