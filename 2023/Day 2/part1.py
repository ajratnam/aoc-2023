with open('input.txt') as file:
    input_data = file.read().replace(':', ';').replace(',', '').split('\n')

total_sum = 0
limits = {'red': 12, 'green': 13, 'blue': 14}

for index, case in enumerate(input_data, 1):
    _, *games = map(str.split, case.split(';'))
    valid_game = True
    for game in games:
        game_value = dict(zip(game[1::2], game[::2]))
        for color, count in game_value.items():
            if int(count) > limits[color]:
                valid_game = False
    if valid_game:
        total_sum += index

print(total_sum)
