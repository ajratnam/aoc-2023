with open('input.txt') as file:
    input_data = file.read().split()

total_sum = 0

for case in input_data:
    digits = list(filter(str.isdigit, case))
    total_sum += int(digits[0] + digits[-1])

print(total_sum)
