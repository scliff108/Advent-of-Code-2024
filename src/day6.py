DAY = 6
FILENAME = 'test.txt'
PATH = f'data/day{DAY}/{FILENAME}'

GUARD = '^'
OBSTACLE = '#'
VISITED = '*'
DIRECTIONS = [
    (-1, 0),  # UP
    (0, 1),   # RIGHT
    (1, 0),   # DOWN
    (0, -1)   # LEFT
]


def read_input(filename: str) -> list[list[str]]:
    with open(filename, 'r') as f:
        data = [list(line.strip()) for line in f.readlines()]
    return data


def find_guard(data: list[list[int]]) -> tuple[int, int]:
    for idx, d in enumerate(data):
        if GUARD in d:
            return idx, d.index(GUARD)
    # If guard not found
    return 0, 0

def part1(data: list[list[str]], guard_location: tuple[int, int]) -> int:
    top = left = -1
    bottom = len(data)
    right = len(data[0])
    y, x = guard_location
    direction = 0

    count = 1
    data[y][x] = VISITED
    move_y, move_x = DIRECTIONS[direction]
    while ((y + move_y > top) and (y + move_y < bottom) and
           (x + move_x > left) and (x + move_x < right)):
        if data[y+move_y][x+move_x] != OBSTACLE:
            # ADVANCE
            y += move_y
            x += move_x
            # CHECK IF WE HAVE BEEN HERE BEFORE
            if data[y][x] != VISITED:
                # MARK VISITED
                data[y][x] = VISITED
                count += 1
        else:  # TURN RIGHT
            direction += 1
            move_y, move_x = DIRECTIONS[(direction) % len(DIRECTIONS)]
    return count


def part2(data: list[list[str]], guard_location: tuple[int, int]) -> int:
    return 0

def main():
    data = read_input(PATH)
    guard_location = find_guard(data)
    p1 = part1(data, guard_location)
    print('Part 1:', p1)

    p2 = part2(data, guard_location)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()