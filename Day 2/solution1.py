invalid_ids = []

with open("input2.txt", "r") as f:
    line = f.readline()
    ranges = line.split(",")
    for r in ranges:
        dash_split = r.split("-")
        range_start = int(dash_split[0])
        range_end = int(dash_split[1])
        for i in range(range_start, range_end + 1):
            num = str(i)
            length = len(num)
            if length % 2 != 0:
                continue
            half = length // 2
            if num[:half] == num[half:]:
                invalid_ids.append(i)
                print(i)

print("Sum of invalid IDs: ", sum(invalid_ids))