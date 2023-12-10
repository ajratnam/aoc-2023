with open('input.txt') as file:
    times, records = map(str.split, file.read().split('\n'))

time, distance = int(''.join(times[1:])), int(''.join(records[1:]))
total_ways = sum(map(lambda t: t * (time - t) > distance, range(time + 1)))

print(total_ways)
