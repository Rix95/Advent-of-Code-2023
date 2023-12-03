file_path = "Python\day02\input.txt"

file = open(file_path, "r")

# default order red blue green

# RED BLUE GREEN DEFAULT MAX VALUES
MAX_COLOR = (12, 13, 14)


# Part 1 & 2
def parse_input(input):
    parsed_games = []
    for line in input:
        # Separate Game ID from rounds
        line = line.strip().split(": ")[1]
        parsed_games.append(line.replace(";", ",").split(", "))
    return parsed_games


# read file used for both
parsed_input = parse_input(file)


def count_max_color(color_value_list) -> tuple(int, int, int):
    color_dict = {"red": 0, "blue": 0, "green": 0}
    print(type(color_value_list))
    # divide value and color
    color_value_list = list(map(lambda ele: ele.split(" "), color_value_list))
    # Prepare values for comparison
    for color_value in color_value_list:
        color_dict[color_value[1]] = max(
            int(color_value[0]), color_dict[color_value[1]]
        )

    return (color_dict["red"], color_dict["green"], color_dict["blue"])


# used for part one
def isValid(color_tuple, max_color):
    for i in range(len(color_tuple)):
        if color_tuple[i] > max_color[i]:
            return False
    return True


def part_one(parsed_input):
    res = 0

    color_tuple_list = list(map(lambda ele: count_max_color(ele), parsed_input))

    for id, color_tuple in enumerate(color_tuple_list):
        if isValid(color_tuple, MAX_COLOR):
            res += id + 1
    return res


def part_two(parsed_input):
    res = 0

    color_tuple_list = list(map(lambda ele: count_max_color(ele), parsed_input))

    res = sum(map(lambda x: x[0] * x[1] * x[2], color_tuple_list))

    return res


print(part_one(parsed_input))
print(part_two(parsed_input))
