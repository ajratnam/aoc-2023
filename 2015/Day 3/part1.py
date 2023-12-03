with open('input.txt') as file:
    input_data = file.read()

houses = {(0, 0)}
santa_position = [0, 0]
axis = "><^v"

for move in input_data:
    index = axis.index(move)
    santa_position[index//2] += (-1) ** index
    houses.add(tuple(santa_position))

print(len(houses))
