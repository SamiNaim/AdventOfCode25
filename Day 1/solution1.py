dial = 50
zeros = 0

with open("input1.txt", "r") as f:
    for line in f:
        direction = line[0]  # get first character
        turn = int(line[1:])
        if direction == "R":
            dial = (dial + turn) % 100
        else:
            dial = (dial - turn) % 100
        if dial == 0:
            zeros += 1

print("Number of zeros: " + str(zeros))