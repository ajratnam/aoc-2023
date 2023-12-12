import re
from itertools import combinations

with open('input.txt') as file:
    space = file.read()

height, width = space.count('\n') + 1, space.index('\n')
expanded = re.sub(fr'\.(?=(.{{{width}}}\.){{{height}}})', '..', space + '\n' + space, flags=re.DOTALL)[:-len(space) - 1]
space = re.sub(r'(\n\.+)(?=\n)', r'\1\1', f'\n{expanded}\n'[1:-1])
total_sum, width = 0, space.index('\n') + 1
for g1, g2 in combinations(re.finditer('#', space), 2):
    g1, g2 = g1.start(), g2.start()
    x1, y1 = g1 % width, g1 // width
    x2, y2 = g2 % width, g2 // width
    total_sum += abs(x1 - x2) + y2 - y1

print(total_sum)
