import math


def main():
    dataset = get_data("5.txt")
    max_found = 0
    for line in dataset:
        print(find_row(line) * 8 + find_col(line))
        if find_row(line) * 8 + find_col(line) > max_found:
            max_found = find_row(line) * 8 + find_col(line)

    print(max_found)


def find_row(l):
    var = [0, "x", 127]
    x = range(6)
    for n in x:
        if l[n] == "F":  # lowerHalf
            var[1] = math.floor((var[2] - var[0]) / 2)
            var[2] = var[2] - var[1]
        if l[n] == "B":  # upperHalf
            var[1] = math.ceil((var[2] - var[0]) / 2)
            var[0] = var[0] + var[1]
    if l[6] == "F":
        return var[0]
    else:
        return var[2]


def find_col(l):
    x = range(6, 9)
    var = [0, "x", 7]
    for n in x:
        if l[n] == "L":  # lowerHalf
            var[1] = math.floor((var[2] - var[0]) / 2)
            var[2] = var[2] - var[1]
        if l[n] == "R":  # upperHalf
            var[1] = math.ceil((var[2] - var[0]) / 2)
            var[0] = var[0] + var[1]
    if l[9] == "L":
        return var[0]
    else:
        return var[2]


def get_data(filename):
    with open(filename) as file:
        data = file.readlines()
    return data


if __name__ == '__main__':
    main()
