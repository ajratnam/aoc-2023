with open('input.txt') as file:
    input_data = file.read().replace(':', '|').split("\n")

total_sum = 0
card_map = [1] * len(input_data)

for pos, card in enumerate(input_data):
    _, correct, mine = map(str.split, card.split('|'))
    card_count = len(set(correct) & set(mine))
    for index in range(card_count):
        card_map[pos + index + 1] += card_map[pos]

print(sum(card_map))
