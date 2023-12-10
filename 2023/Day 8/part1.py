from itertools import cycle
from re import match

with open('input.txt') as file:
    steps, _, *nodes = file.read().split('\n')

instructions = cycle(map('LR'.index, steps))
node_map = {}

for node in nodes:
    cnode, lnode, rnode = match(r'(...) = \((...), (...)\)', node).groups()
    node_map[cnode] = [lnode, rnode]

node, steps = 'AAA', 0
while node != 'ZZZ':
    node = node_map[node][next(instructions)]
    steps += 1

print(steps)
