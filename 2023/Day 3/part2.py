import re
from collections import defaultdict
from math import prod

with open('input.txt') as file:
    input_data = file.read().split()

schematic = ['.' * (len(input_data[0]) + 2)] * 2
schematic[1:1] = map(".{}.".format, input_data)
total_sum = 0

gear_list = defaultdict(list)

for index, row in enumerate(schematic[1:-1], 1):
    for number in re.finditer(r'\d+', row):
        start, stop = number.span()
        for row_offset, section in enumerate(schematic[index - 1:index + 2]):
            for col_offset, char in enumerate(section[start - 1:stop + 1]):
                if char not in '0123456789.':
                    gear_list[(index + row_offset - 1, start + col_offset - 1)].append(int(number.group()))

for parts in gear_list.values():
    if len(parts) == 2:
        total_sum += prod(parts)

print(total_sum)
