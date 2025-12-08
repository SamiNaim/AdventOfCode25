beam_split = 0
grid = []

def beam_down(row, column):
    global beam_split
    while grid[row][column] == ".":
        grid[row][column] = "|"
        if row == len(grid) - 1:
            return False, False
        row += 1
    if grid[row][column] == "|":
        return False, False
    beam_split += 1
    return (row, column - 1), (row, column + 1)

with open("input7.txt", "r") as f:
    for line in f:
        line = line.strip()
        grid_line = []
        for char in line:
            grid_line.append(char)
        grid.append(grid_line)

s_pos = 0
for i, char in enumerate(grid[0]):
    if char == "S":
        s_pos = i
        break

indices = set()
indices.add((1, s_pos))
while len(indices) > 0:
    (r, c) = indices.pop()
    a, b = beam_down(r, c)
    if not a:
        continue
    indices.add(a)
    indices.add(b)


print("Beam splits: ", beam_split)