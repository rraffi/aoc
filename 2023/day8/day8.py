with open("in.txt") as f:
    data = f.read().splitlines()

directions = list(data[0])

def get_routes(s):
    parts = s.split("=")

    first_part = parts[0].strip()
    second_part = parts[1].strip().strip("()")
    second_part_list = [x.strip() for x in second_part.split(",")]

    return [first_part, second_part_list]


routes = []
for i in range(2, len(data)):
    routes.append(get_routes(data[i]))


def number_of_steps(directions, routes):
    steps = 0
    dest = 'AAA'
    while dest != 'ZZZ':
        for d in directions:
            for i in range(len(routes)):
                if routes[i][0] == dest:
                    if d == 'L':
                        dest = routes[i][1][0]
                    elif d == 'R':
                        dest = routes[i][1][1]
                    steps += 1
                    break
    return steps


# print(number_of_steps(directions, routes))

def get_routes(s):
    parts = s.split("=")

    first_part = parts[0].strip()
    second_part = parts[1].strip().strip("()")
    second_part_list = [x.strip() for x in second_part.split(",")]

    return [first_part, second_part_list]


routes = []
for i in range(2, len(data)):
    routes.append(get_routes(data[i]))


def number_of_steps(directions, routes):
    steps = 0
    dest = 'AAA'
    while dest != 'ZZZ':
        for d in directions:
            for i in range(len(routes)):
                if routes[i][0] == dest:
                    if d == 'L':
                        dest = routes[i][1][0]
                    elif d == 'R':
                        dest = routes[i][1][1]
                    steps += 1
                    break
    return steps


# print(number_of_steps(directions, routes))

def starting_nodes(routes):
    nodes = []
    for i in range(len(routes)):
        if routes[i][0].endswith('A'):
            nodes.append(routes[i][0])

    return nodes


def number_of_steps_from_nodes(directions, routes):
    nodes = starting_nodes(routes)

    for node in nodes:
        steps = 0
        dest = node
        while not dest.endswith('Z'):
            for d in directions:
                for i in range(len(routes)):
                    if routes[i][0] == dest:
                        if d == 'L':
                            dest = routes[i][1][0]
                        elif d == 'R':
                            dest = routes[i][1][1]
                        steps += 1
                        break
        print(node, steps)


if __name__ == "__main__":
    number_of_steps_from_nodes(directions, routes)