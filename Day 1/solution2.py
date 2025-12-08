dial = 50
zeros = 0

with open("input1.txt", "r") as f:
    for line in f:
        direction = line[0]  # get first character
        turn = int(line[1:])
        if direction == "R":
            new_dial = dial + turn
        else:
            new_dial = dial - turn
        mod_dial = new_dial % 100
        if mod_dial == 0:
            wraps = abs(new_dial // 100)
            if new_dial <= 0:
                wraps += 1
            zeros += wraps
        else:
            if dial == 0:
                zeros += abs(new_dial) // 100
            else:
                zeros += abs(new_dial // 100)
        dial = mod_dial

print("Number of zeros: " + str(zeros))