DAY = 2
FILENAME = 'input.txt'
PATH = f'data/day{DAY}/{FILENAME}'


def read_input(filename: str) -> list[list[int]]:
    with open(filename, 'r') as f:
        return [list(map(int, line.split())) for line in f]


def is_safe(report: list[int]) -> bool:
    multiplier = 1 if report[0] > report[1] else -1

    for next_idx, level in enumerate(report[:-1], 1):
        next_level = report[next_idx]
        difference = multiplier * (level - next_level)
        if difference < 1 or difference > 3:
            return False
    return True


def part1(reports: list[list[int]]) -> int:
    return sum(is_safe(report) for report in reports)


def part2(reports: list[list[int]]) -> int:
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    safe_count += 1
                    break

    return safe_count


def main():
    reports = read_input(PATH)

    p1 = part1(reports)
    print('Part 1:', p1)

    p2 = part2(reports)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()