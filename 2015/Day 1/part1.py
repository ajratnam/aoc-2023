with open('input.txt') as file:
    input_data = file.read()

floor = 0
for count, step in enumerate(input_data):
    floor += {'(': 1, ')': -1}[step]
    if floor == -1:
        break

print(count + 1)
