with open("in.txt") as f:
    data = f.read().splitlines()


# Function to get the entire number surrounding a position
def get_full_number(data, i, j):
    # Expand left to find the start of the number
    start_j = j
    while data[i][start_j - 1].isdigit():
        start_j -= 1

    # Expand right to find the end of the number
    end_j = j
    while data[i][end_j + 1].isdigit():
        end_j += 1

    # Extract the full number
    return int(''.join(data[i][start_j:end_j + 1]))


def sum_id_numbers(data):
    # Function to check if a cell contains a symbol (excluding periods)
    def is_symbol(cell):
        return not cell.isdigit() and cell != '.'

    # Set to keep track of all id numbers
    id_numbers = set()

    # Iterate over the data to find symbols and their adjacent numbers
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if is_symbol(cell):
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if data[ni][nj].isdigit():
                        print(get_full_number(data, ni, nj))
                        id_numbers.add(get_full_number(data, ni, nj))

    print(id_numbers)
    # Sum of all id numbers
    return sum(id_numbers)

# Example usage

print(sum_id_numbers(data))
