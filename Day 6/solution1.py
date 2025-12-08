grand_total = 0
operations = []

with open("input6.txt", "r") as f:
    for line in f:
        line = line.strip()
        operations.append(line.split())

operation_size = len(operations[0])
for i in range(operation_size):
    if operations[4][i] == "+":
        grand_total += (int(operations[0][i]) + int(operations[1][i]) + int(operations[2][i]) + int(operations[3][i]))
    else:
        grand_total += (int(operations[0][i]) * int(operations[1][i]) * int(operations[2][i]) * int(operations[3][i]))

print("Grand total: ", grand_total)