from collections import Counter

with open('input.txt') as file:
    input_data = map(str.split, file.read().split('\n'))

card_strength = '23456789TJQKA'
total_sum = 0
get_strength = lambda card: (sorted(Counter(card[0]).values())[::-1], *map(card_strength.index, card[0]))

order = sorted(input_data, key=get_strength)
for rank, (_, bid) in enumerate(order, 1):
    total_sum += int(bid) * rank

print(total_sum)
