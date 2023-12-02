import Python.file_reader as file_reader

file_path = "Python\\Day 01\\input_part1.txt"

file = file_reader.read_file(file_path)


# Part 1
def getLines(file) -> List[str]:
    line_list = []
    for line in file:
        line_list.append(line.strip())
    return line_list
    #    line_length = len(line_without_trail) not used right now


def get_digits(line: str) -> int:
    for char in line:
        if char.isnumeric():
            first_digit = char
            break

    for char in reversed(line_without_trail):
        if char.isnumeric():
            second_digit = char
            break
    result += int(first_digit + second_digit)


def convert_digit_substrings(line_list: List[str]) -> List[str]:
    digit_dictionary = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    new_line_list = line_list.copy()
    for line in new_line_list:
        for key in digit_dictionary:
            if key in line:
                new_line_list = line.replace(key, digit_dictionary[key])
    return new_line_list


def part_one(file):
    line_list = getLines(file)

    res = 0
    for line in line_list:
        res += get_digits(line)
    return res


def part_two(file):
    line_list = convert_digit_substrings(getLines(file))
    res = 0
    for line in line_list:
        res += get_digits(line)
    return res


# Part 1 result
print(part_one(file))
# Part 2 result
print(part_two(file))
