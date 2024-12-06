DAY = 1
FILENAME = 'input.txt'
PATH = f'data/day{DAY}/{FILENAME}'


def read_input(filename: str) -> tuple[list[int], list[int]]:
    l1 = []
    l2 = []
    with open(filename, 'r') as f:
        for line in f:
            a, b = line.split()
            l1.append(int(a))
            l2.append(int(b))
    return l1, l2


def part1(l1: list, l2: list) -> int:
    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)

    total = 0
    for i in range(len(sorted_l1)):
        total += abs(sorted_l1[i] - sorted_l2[i])
    
    return total


def part2(l1: list, l2: list) -> int:
    counts = dict()
    for item in l2:
        counts[item] = counts.get(item, 0) + 1
    
    total = 0
    for item in l1:
        total += counts.get(item, 0) * item

    return total


def main():
    l1, l2 = read_input(PATH)
    p1 = part1(l1, l2)
    print('Part 1:', p1)

    p2 = part2(l1, l2)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()