DAY = 4
FILENAME = 'input.txt'
PATH = f'data/day{DAY}/{FILENAME}'
VERBOSE = False


def read_input(filename: str) -> list[int]:
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def test_word(word: str, direction: str, r: int, c: int, verbose: bool=False) -> bool:
    if word == 'XMAS':
        if verbose:
            print(direction, r, c, word)
        return True
    return False


def part1(data: list[int], verbose: bool=False) -> int:
    total = 0

    for r_idx, row in enumerate(data):
        for c_idx, col in enumerate(row):
            if col == 'X':
                # Forward
                if c_idx + 3 < len(row):
                    forward = row[c_idx:c_idx+4]
                    total += test_word(forward, 'forward', r_idx, c_idx, verbose)
                # Backward
                if c_idx - 3 >= 0:
                    backward = row[c_idx-3:c_idx+1][::-1]
                    total += test_word(backward, 'backward', r_idx, c_idx, verbose)
                # Up
                if r_idx - 3 >= 0:
                    up = ''.join([data[r][c_idx] for r in range(r_idx-3, r_idx+1)][::-1])
                    total += test_word(up, 'up', r_idx, c_idx, verbose)
                # Down
                if r_idx + 3 < len(data):
                    down = ''.join([data[r][c_idx] for r in range(r_idx, r_idx+4)])
                    total += test_word(down, 'down', r_idx, c_idx, verbose)
                # Up and Right
                if r_idx - 3 >= 0 and c_idx + 3 < len(row):
                    up_right = ''.join([data[r_idx-i][c_idx+i] for i in range(4)])
                    total += test_word(up_right, 'up and right', r_idx, c_idx, verbose)
                # Up and Left
                if r_idx - 3 >= 0 and c_idx - 3 >= 0:
                    up_left = ''.join([data[r_idx-i][c_idx-i] for i in range(4)])
                    total += test_word(up_left, 'up and left', r_idx, c_idx, verbose)
                # Down and Right
                if r_idx + 3 < len(data) and c_idx + 3 < len(row):
                    down_right = ''.join([data[r_idx+i][c_idx+i] for i in range(4)])
                    total += test_word(down_right, 'down and right', r_idx, c_idx, verbose)
                # Down and Left
                if r_idx + 3  < len(data) and c_idx - 3 >= 0:
                    down_left = ''.join([data[r_idx+i][c_idx-i] for i in range(4)])
                    total += test_word(down_left, 'down and left', r_idx, c_idx, verbose)
    return total


def part2(data: list[int]) -> int:
    total = 0
    matches = [
        ['S','S','M','M'],  # S top, M bottom
        ['M','S','M','S'],  # S right, M left
        ['M','M','S','S'],  # S bottom, M top
        ['S','M','S','M']   # S left, M right
    ]

    for r_idx, row in enumerate(data):
        for c_idx, col in enumerate(row):
            if col == 'A':
                if r_idx >= 1 and r_idx <= len(data) - 2 and c_idx >= 1 and c_idx <= len(row) - 2:
                    neighbors = [
                        data[r_idx - 1][c_idx - 1],  # Top left
                        data[r_idx - 1][c_idx + 1],  # Top right
                        data[r_idx + 1][c_idx - 1],  # Bottom left
                        data[r_idx + 1][c_idx + 1]   # Bottom right
                    ]
                    if neighbors in matches:
                        total += 1
    return total


def main():
    data = read_input(PATH)
    p1 = part1(data, VERBOSE)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()