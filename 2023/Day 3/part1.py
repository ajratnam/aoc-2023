import re

with open('input.txt') as file:
    input_data = file.read().split()

schematic = ['.' * (len(input_data[0]) + 2)] * 2
schematic[1:1] = map(".{}.".format, input_data)
total_sum = 0

for index, row in enumerate(schematic[1:-1], 1):
    for number in re.finditer(r'\d+', row):
        start, stop = number.span()
        for section in schematic[index - 1:index + 2]:
            if re.sub(r'[\d\.]', '', section[start - 1:stop + 1]):
                total_sum += int(number.group())
                break

print(total_sum)
