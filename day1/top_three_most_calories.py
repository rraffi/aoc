import most_calorific_elf


def top_three_max(data: list) -> list:
    top_three = []
    for _ in range(3):
        top_three.append(data.pop(data.index(max(data))))

    print(top_three)
    print(data)
    return top_three


print(sum(top_three_max(most_calorific_elf.elves_calories)))