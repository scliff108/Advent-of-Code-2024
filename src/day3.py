import re

DAY = 3
FILENAME = 'input.txt'
PATH = f'data/day{DAY}/{FILENAME}'

def part1(s: str) -> int:
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    matches = re.findall(pattern, s)

    total = 0
    for m in matches:
        total += int(m[0]) * int(m[1])
    return total


def part2(s: str) -> int:
    pattern = r"(do\(\))|(don't\(\))|mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    matches = re.findall(pattern, s)

    enabled = True
    total = 0
    for m in matches:
        if m[0]:
            enabled = True
        elif m[1]:
            enabled = False
        else: 
            if enabled:
                total += int(m[2]) * int(m[3])
    return total


def main():
    with open(PATH, 'r') as f:
        s = ''.join(map(str.strip, f.readlines()))
    p1 = part1(s)
    print('Part 1:', p1)

    p2 = part2(s)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()