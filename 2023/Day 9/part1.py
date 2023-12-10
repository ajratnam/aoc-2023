import numpy as np

with open('input.txt') as file:
    input_data = map(str.split, file.read().split('\n'))

total_sum = 0


def get_next(sequence):
    if len(set(sequence)) == 1:
        return sequence[0]
    return sequence[-1] + get_next(np.diff(sequence))


for history in input_data:
    total_sum += get_next([*map(int, history)])

print(total_sum)
