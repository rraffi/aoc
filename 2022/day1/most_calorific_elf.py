with open("day1.txt") as f:
    data = f.read().splitlines()


cal = 0
elves_calories = []
for item in data:
    if item:
        cal = cal + int(item)
    else:
        elves_calories.append(cal)
        cal = 0

print(max(elves_calories))


