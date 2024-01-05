import fileinput
from itertools import cycle
import math

with open("in.txt") as f:
    data = f.read().splitlines()

dirns = [int(c == 'R') for c in data[0].strip()]

nodes = {}
for line in data[2:]:
    n, _, *rest = line.strip().split()
    nodes[n] = [e.strip('(),') for e in rest]

def find(node: str, end: str) -> int:
    for n, d in enumerate(cycle(dirns), 1):
        node = nodes[node][d]
        if node.endswith(end):
            return n

print('P1 =', find('AAA', 'ZZZ'))

startnodes = [n for n in nodes if n.endswith('A')]
print('P2 =', math.lcm(*(find(n, 'Z') for n in startnodes)))
