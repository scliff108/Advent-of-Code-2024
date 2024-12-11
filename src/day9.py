DAY = 9
FILENAME = 'test.txt'
PATH = f'data/day{DAY}/{FILENAME}'


def read_input1(filename: str) -> list:
    data = []
    with open(filename, 'r') as f:
        disk_image = list(map(int, list(f.readline().strip())))
        file_id = 0
        for block_num, block_len in enumerate(disk_image):
            if block_num % 2:
                for i in range(block_len):
                    data.append('.')
            else:
                for i in range(block_len):
                    data.append(file_id)
                file_id += 1
    return data


def checksum(data: list):
    total = 0
    for block, file_id in enumerate(data):
        if file_id != '.':
            total += file_id * block
    return total


def part1(data: list) -> int:
    left_ptr = 0
    right_ptr = len(data) - 1

    while left_ptr < right_ptr:
        # Check pointers
        if data[left_ptr] != '.':
            left_ptr += 1
        if data[right_ptr] == '.':
            right_ptr -= 1

        # Swap
        if data[left_ptr] == '.' and data[right_ptr] != '.':
            data[left_ptr] = data[right_ptr]
            data[right_ptr] = '.'
            left_ptr += 1
            right_ptr -= 1
    
    return checksum(data)


def part2(data: list[int]) -> int:
    return 0

def main():
    data = read_input1(PATH)
    p1 = part1(data)
    print('Part 1:', p1)

    p2 = part2(data)
    print('Part 2:', p2)


if __name__ =='__main__':
    main()