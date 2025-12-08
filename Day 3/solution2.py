joltages = []

def get_highest_number(line, start, end):
    highest_num = 1
    index = start
    for i in range(start, end):
        num = int(line[i])
        if num > highest_num:
            highest_num = num
            index = i
    return highest_num, index + 1


with open("input3.txt", "r") as f:
    for line in f:
        line = line.strip()
        number = 0
        start_index = 0
        for i in range(11, -1, -1):
            highest_num, start_index = get_highest_number(line, start_index, len(line) - i)
            number += highest_num * pow(10, i)
        joltages.append(number)

print("Total output joltage: ", sum(joltages))