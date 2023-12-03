with open('input.txt') as file:
    input_data = file.read()

input_data = input_data[::2] + ' ' + input_data[1::2]

houses = {(0, 0)}
santa_position = [0, 0]
axis = "><^v"

for move in input_data:
    if move == ' ':
        santa_position = [0, 0]
        continue
    index = axis.index(move)
    santa_position[index // 2] += (-1) ** index
    houses.add(tuple(santa_position))

print(len(houses))
