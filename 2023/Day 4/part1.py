with open('input.txt') as file:
    input_data = file.read().replace(':', '|').split("\n")

total_sum = 0

for card in input_data:
    _, correct, mine = map(str.split, card.split('|'))
    total_sum += int(2 ** (len(set(correct) & set(mine)) - 1))

print(total_sum)
