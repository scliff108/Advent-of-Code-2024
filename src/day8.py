from collections import defaultdict
from itertools import combinations

DAY = 8
FILENAME = 'input.txt'
PATH = f'data/day{DAY}/{FILENAME}'


def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        data = [list(line.strip()) for line in f.readlines()]
    return data


def test_within_bounds(antinode: tuple[int, int], boundaries: tuple[int, int]) -> bool:
    return ((antinode[0] >= 0 and antinode[0] <= boundaries[0]) and
            (antinode[1] >= 0 and antinode[1] <= boundaries[1]))


def part1(data: list[str]) -> int:
    characters = defaultdict(list)
    boundaries = (len(data) - 1, len(data[0]) - 1)

    # Get the location of each node
    for r_idx, row in enumerate(data):
        for c_idx, col in enumerate(row):
            if col != '.':
                characters[col].append((r_idx, c_idx))

    antinodes = set()
    for char, locations in characters.items():
        combos = combinations(locations, 2)
        for combo in combos:
            row_delta = combo[0][0] - combo[1][0]
            col_delta = combo[0][1] - combo[1][1]

            antinode1 = (combo[0][0] - 2 * row_delta, combo[0][1] - 2 * col_delta)
            antinode2 = (combo[0][0] + row_delta, combo[0][1] + col_delta)

            if test_within_bounds(antinode1, boundaries):
                antinodes.add(antinode1)
            
            if test_within_bounds(antinode2, boundaries):
                antinodes.add(antinode2)

    return len(antinodes)


def part2(data: list[str]) -> int:
    characters = defaultdict(list)
    boundaries = (len(data) - 1, len(data[0]) - 1)

    # Get the location of each node
    for r_idx, row in enumerate(data):
        for c_idx, col in enumerate(row):
            if col != '.':
                characters[col].append((r_idx, c_idx))

    antinodes = set()
    for char, locations in characters.items():
        combos = combinations(locations, 2)
        for combo in combos:
            antinodes.add(combo[0])
            antinodes.add(combo[1])
            row_delta = combo[0][0] - combo[1][0]
            col_delta = combo[0][1] - combo[1][1]

            antinode1 = (combo[0][0] - 2 * row_delta, combo[0][1] - 2 * col_delta)
            antinode2 = (combo[0][0] + row_delta, combo[0][1] + col_delta)
            
            while test_within_bounds(antinode1, boundaries):
                antinodes.add(antinode1)
                antinode1 = (antinode1[0] - row_delta, antinode1[1] - col_delta)

            while test_within_bounds(antinode2, boundaries):
                antinodes.add(antinode2)
                antinode2 = (antinode2[0] + row_delta, antinode2[1] + col_delta)

    return len(antinodes)


def main():
    data = read_input(PATH)
    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()
