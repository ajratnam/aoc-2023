from math import prod

with open('input.txt') as file:
    input_data = file.read().replace(':', ';').replace(',', '').split('\n')

total_sum = 0
limits = {'red': 12, 'green': 13, 'blue': 14}

for index, case in enumerate(input_data, 1):
    _, *games = map(str.split, case.split(';'))
    min_count = {'red': 0, 'green': 0, 'blue': 0}
    for game in games:
        game_value = dict(zip(game[1::2], game[::2]))
        for color, count in game_value.items():
            min_count[color] = max(min_count.get(color, 0), int(count))
    total_sum += prod(min_count.values())

print(total_sum)
