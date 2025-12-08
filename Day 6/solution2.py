grand_total = 0
split_sizes = []
operations = []

with open("input6.txt", "r") as f:
    for line in f:
        if line[0] == "+":
            line = line.removesuffix("\n")
            line += " "
            replace_plus = line.replace("*", "+")
            split_plus = replace_plus.split("+")
            split_plus.pop(0)
            split_sizes = list(len(x) for x in split_plus)

with open("input6.txt", "r") as f:
    for line in f:
        line_list = []
        curr_index = 0
        for segment in split_sizes:
            line_list.append(line[curr_index:(curr_index + segment)])
            curr_index += segment + 1
        operations.append(line_list)

operation_size = len(operations[0])
for i in range(operation_size):
    max_char = len(operations[0][i])
    if operations[4][i][0] == "+":
        total = 0
        for j in range(max_char):
            number = operations[0][i][j] + operations[1][i][j] + operations[2][i][j] + operations[3][i][j]
            total += int(number)
        grand_total += total
    else:
        total = 1
        for j in range(max_char):
            number = operations[0][i][j] + operations[1][i][j] + operations[2][i][j] + operations[3][i][j]
            total *= int(number)
        grand_total += total

print("Grand total: ", grand_total)