joltages = []

with open("input3.txt", "r") as f:
    for line in f:
        line = line.strip()
        left_num = 1
        left_num_index = 0
        right_num = 1
        for i in range(len(line) - 1):
            num = int(line[i])
            if num > left_num:
                left_num = num
                left_num_index = i
        for i in range(left_num_index + 1, len(line)):
            num = int(line[i])
            if num > right_num:
                right_num = num
        joltages.append(left_num * 10 + right_num)

print("Total output joltage: ", sum(joltages))