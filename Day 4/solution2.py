paper_rolls = 0

grid = []
with open("input4.txt", "r") as f:
    row_size = len(f.readline().strip()) + 2

grid.append([0]*row_size)
with open("input4.txt", "r") as f:
    for line in f:
        line = line.strip()
        row = []
        row.append(0)
        for i in range(len(line)):
            if line[i] == '@':
                row.append(1)
            else:
                row.append(0)
        row.append(0)
        grid.append(row)
grid.append([0]*row_size)

grid_size = len(grid)
removable = True
while removable:
    removable = False
    for i in range(grid_size):
        for j in range(row_size):
            if grid[i][j] == 1:
                adjacent = 0
                adjacent += grid[i-1][j-1]
                adjacent += grid[i][j-1]
                adjacent += grid[i+1][j-1]
                adjacent += grid[i-1][j+1]
                adjacent += grid[i][j+1]
                adjacent += grid[i+1][j+1]
                adjacent += grid[i-1][j]
                adjacent += grid[i+1][j]
                if adjacent < 4:
                    grid[i][j] = 0
                    removable = True
                    paper_rolls += 1

print("Total accessible rolls of paper: ", paper_rolls)