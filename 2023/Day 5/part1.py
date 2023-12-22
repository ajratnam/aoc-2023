with open('input.txt') as file:
    seeds, *almanac = file.read().split('\n\n')

locations = [*map(int, seeds.split()[1:])]

for conversion_map in almanac:
    paths = *map(lambda path: [*map(int, path.split())], conversion_map.split('\n')[1:]),
    for seed_no, seed_loc in enumerate(locations):
        for destination, source, length in paths:
            if source <= seed_loc < source + length:
                locations[seed_no] = destination + seed_loc - source
                break

print(min(locations))
