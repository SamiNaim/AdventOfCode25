from time import sleep

parallel_split = 0
grid = []
indices = []

def process_line(row):
    global grid
    for column in range(len(grid[row])):
        top = grid[row - 1][column]
        if top != 0:
            if grid[row][column] == -1:
                grid[row][column - 1] += top
                grid[row][column + 1] += top
            elif top != -1:
                grid[row][column] += top

with open("input7.txt", "r") as f:
    for line in f:
        line = line.strip()
        grid_line = []
        for char in line:
            grid_line.append(char)
        grid.append(grid_line)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            grid[i][j] = 0
        elif grid[i][j] == "^":
            grid[i][j] = -1
        elif grid[i][j] == "S":
            grid[i][j] = -2

s_pos = 0
for i, num in enumerate(grid[0]):
    if num == -2:
        grid[1][i] = 1

for i in range(2, len(grid)):
    process_line(i)

for g in grid:
    print(g)

parallel_split = sum(int(x) for x in grid[len(grid) - 1])
print("Beam splits: ", parallel_split)

"""
['0', '0', '0', '0', '0',  '0', '0',  'S', '0',  '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '0',  '0', '0',  '1', '0',  '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '0',  '0', '1',  '^', '1',  '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '0',  '0', '1',  '0', '1',  '0', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '0',  '1', '^',  '2', '^',  '1', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '0',  '1', '0',  '2', '0',  '1', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '1',  '^', '3',  '^', '3',  '^', '1', '0', '0', '0', '0']
['0', '0', '0', '0', '1',  '0', '3',  '0', '3',  '0', '1', '0', '0', '0', '0']
['0', '0', '0', '1', '^',  '4', '^',  '3', '3',  '1', '^', '1', '0', '0', '0']
['0', '0', '0', '1', '0',  '4', '0',  '3', '3',  '1', '0', '1', '0', '0', '0']
['0', '0', '1', '^', '5',  '^', '4',  '3', '4',  '^', '2', '^', '1', '0', '0']
['0', '0', '1', '0', '5',  '0', '4',  '3', '4',  '0', '2', '0', '1', '0', '0']
['0', '1', '^', '1', '5',  '4', '^',  '7', '4',  '0', '2', '1', '^', '1', '0']
['0', '1', '0', '1', '5',  '4', '0',  '7', '4',  '0', '2', '1', '0', '1', '0']
['1', '^', '2', '^', '10', '^', '11', '^', '11', '^', '2', '1', '1', '^', '1']
['1', '0', '2', '0', '10', '0', '11', '0', '11', '0', '2', '1', '1', '0', '1']
"""