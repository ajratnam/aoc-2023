import numpy as np

with open('input.txt') as file:
    input_data = map(str.split, file.read().split('\n'))

total_sum = 0


def get_prev(sequence):
    if len(set(sequence)) == 1:
        return sequence[0]
    return sequence[0] - get_prev(np.diff(sequence))


for history in input_data:
    total_sum += get_prev([*map(int, history)])

print(total_sum)
