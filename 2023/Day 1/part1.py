with open('input.txt') as file:
    input_data = file.read().split()

total_sum = 0


def get_digits(data):
    return list(filter(str.isdigit, data))


for case in input_data:
    digits = get_digits(case)
    total_sum += int(digits[0]+digits[-1])

print(total_sum)
