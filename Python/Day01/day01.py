file_path = "Python\day01\input_part1.txt"

file = open(file_path, "r")


# Part 1
def getLines(file):
    line_list = []
    for line in file:
        line_list.append(line.strip())
    return line_list


def get_digits(line: str):
    for char in line:
        if char.isnumeric():
            first_digit = char
            break

    for char in reversed(line):
        if char.isnumeric():
            second_digit = char
            break
    return int(first_digit + second_digit)


def convert_digit_substrings(line):
    digit_dic = {
        "one": "o1ne",
        "two": "t2wo",
        "three": "t3hree",
        "four": "f4our",
        "five": "f5ive",
        "six": "s6ix",
        "seven": "s7even",
        "eight": "e8ight",
        "nine": "n9ine",
    }

    line_length = len(line)
    for digit in digit_dic:
        if digit in line:
            line = line.replace(digit, digit_dic[digit])

    return line


def part_one(input_list):
    res = 0
    for line in input_list:
        res += get_digits(line)
    return res


def part_two(input_list):
    res = 0
    test_list = []
    for line in input_list:
        temp = get_digits(convert_digit_substrings(line))
        res += temp

    return res


input_list = getLines(file)


# Part 1 result
print(part_one(input_list))
# Part 2 result
print(part_two(input_list))
