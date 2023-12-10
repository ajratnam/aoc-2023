with open('input.txt') as file:
    pipes = file.read()

pm = {
    '|': {'N': 'N', 'S': 'S'},
    '-': {'E': 'E', 'W': 'W'},
    'L': {'S': 'E', 'W': 'N'},
    'J': {'S': 'W', 'E': 'N'},
    '7': {'N': 'W', 'E': 'S'},
    'F': {'N': 'E', 'W': 'S'},
    '.': {'.': '.'}
}

l = pipes.index('\n') + 1
sp = pipes.index('S')  # starting pipe location
n = pipes[sp - l] if sp >= l else "."
w = pipes[sp - 1] if sp % l else "."
e = pipes[sp + 1] if (sp + 2) % l else "."
s = pipes[sp + l] if sp + l < len(pipes) else "."
pipe = ("N" in pm[n]) << 3 | ("W" in pm[w]) << 2 | ("E" in pm[e]) << 1 | ("S" in pm[s])
pipe = "|LFJ7-"[pipe % 8 - 1]

pos_map = {"N": -l, "W": -1, "E": 1, "S": l}
cm = list(pm[pipe].values())[0]  # current move
pos, steps = sp + pos_map[cm], 1

while pos != sp:
    cm = pm[pipes[pos]][cm]
    pos += pos_map[cm]
    steps += 1

print(steps // 2)
