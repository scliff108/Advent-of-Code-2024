DAY = 7
FILENAME = 'input.txt'
PATH = f'data/day{DAY}/{FILENAME}'


def read_input(filename: str) -> list[tuple[int, list[int]]]:
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            test_value, equation = line.strip().split(': ')
            test_value = int(test_value)
            equation = list(map(int, equation.split(' ')))
            data.append((test_value, equation))
    return data


def operate(total: int, numbers: list[int], target: int) -> int:
    # Base Case
    if not numbers:
        return total == target
    
    next_num = numbers[0]
    addition = total + next_num
    multiplication = total * next_num

    # Recursive Call
    return operate(addition, numbers[1:], target) or operate(multiplication, numbers[1:], target)


def operate2(total: int, numbers: list[int], target: int) -> int:
    # Base Case
    if not numbers:
        return total == target
    
    next_num = numbers[0]
    addition = total + next_num
    multiplication = total * next_num
    concatenation = int(str(total) + str(next_num))

    # Recursive Call
    return operate2(addition, numbers[1:], target) or operate2(multiplication, numbers[1:], target) or operate2(concatenation, numbers[1:], target)


def part1(data: list[tuple[int, list[int]]]) -> int:
    return sum(test_value for (test_value, numbers) in data if operate(numbers[0], numbers[1:], test_value))


def part2(data: list[tuple[int, list[int]]]) -> int:
    return sum(test_value for (test_value, numbers) in data if operate2(numbers[0], numbers[1:], test_value))


def main():
    data = read_input(PATH)
    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()