from itertools import chain, combinations

min_presses = 0

def flip_lights(lights, flips):
    for flip in flips:
        lights[flip] = not lights[flip]

def powerset(lst):
    return chain.from_iterable(combinations(lst, r) for r in range(1, len(lst)+1))

with open("input10.txt", "r") as f:
    for line in f:
        line = line.strip()
        line = line.split()
        light = line.pop(0)
        lights = int(''.join('1' if c == '#' else '0' for c in reversed(light.strip('[]'))), 2)
        line.pop()
        buttons = []
        for b in line:
            button = list(map(int, b.strip("()").split(",")))
            pattern = 0
            for bb in button:
                pattern += 1 << bb
            buttons.append(pattern)
        power_set = powerset(buttons)
        min_p = pow(2, len(buttons))
        for subset in power_set:
            if len(subset) >= min_p:
                continue
            x = 0
            for b in subset:
                x ^= b
            if x == lights:
                min_p = len(subset)
        min_presses += min_p

print("The fewest button presses: ", min_presses)