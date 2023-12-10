with open('input.txt') as file:
    times, records = file.read().split('\n')

total_prod = 1
for record in zip(times.split()[1:], records.split()[1:]):
    time, distance = map(int, record)
    total_prod *= sum(map(lambda t: t * (time - t) > distance, range(time + 1)))

print(total_prod)
