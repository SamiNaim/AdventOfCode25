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
            if length < 2:
                continue
            for j in range(2, length + 1):
                if length % j == 0:
                    part_size = length // j
                    parts = [num[k:k+part_size] for k in range(0, length, part_size)]
                    if len(set(parts)) == 1:
                        invalid_ids.append(i)
                        break

print("Sum of invalid IDs: ", sum(invalid_ids))