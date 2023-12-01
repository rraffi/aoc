import calibrations_sum


def replace_number_words_with_numerals(s: str):
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    valid_ints = []
    for pos in range(len(s)):
        if s[pos].isnumeric():
            valid_ints.append(s[pos])

        # loop through each segment of the string and check if it matches a number word
        for i, word in enumerate(number_map):
            if s[pos: pos + len(word)] == word:
                valid_ints.append(str(i + 1))

    return valid_ints


with open("calibrations.txt") as f:
    data = f.read().splitlines()


new_data = []
for item in data:
    new_item = replace_number_words_with_numerals(item)
    new_data.append(new_item)

if __name__ == "__main__":
    print(calibrations_sum.calculate_sum(new_data))