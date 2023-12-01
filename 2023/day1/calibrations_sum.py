with open("calibrations.txt") as f:
    data = f.read().splitlines()


def get_first_last(item: str):
    first_last = []
    for value in item:
        if value.isnumeric():
            first_last.append(value)
    return first_last[0] + first_last[-1]


def calculate_sum(data):
    sum = 0
    for item in data:
        sum = sum + int(get_first_last(item))

    return sum


if __name__ == "__main__":
    print(calculate_sum(data))
