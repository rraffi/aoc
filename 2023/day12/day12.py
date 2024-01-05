with open("t.txt") as f:
    data = f.read().splitlines()

springs, groups = [], []
for line in data:
    springs.append(line.split(" ")[0])
    groups.append(line.split(" ")[1])

# print(springs)
# print(groups)

arrs = []

for i, spring in enumerate(springs):
    group = groups[i].split(',')
    print(group)
    # damaged = spring.count("#")
    # if damaged