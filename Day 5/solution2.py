range_list = []

def update_ranges(ranges, start_id, end_id):
    new = True
    for i, (s, e) in enumerate(ranges):
        if start_id == s:
            if end_id > e:
                ranges[i] = (start_id, end_id)
                new = False
                break
            else:
                new = False
                break
        elif start_id < s:
            if end_id > e:
                ranges[i] = (start_id, end_id)
                new = False
                break
            elif end_id >= s:
                ranges[i] = (start_id, e)
                new = False
                break
        else:
            if start_id <= e:
                if end_id > e:
                    ranges[i] = (s, end_id)
                    new = False
                    break
                else:
                    new = False
                    break
    if new:
        ranges.append((start_id, end_id))

with open("input5.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        dash_split = line.split("-")
        start_id = int(dash_split[0])
        end_id = int(dash_split[1])
        update_ranges(range_list, start_id, end_id)

updated_ranges = []
list_size = len(range_list)
while len(updated_ranges) != list_size:
    updated_ranges = []
    list_size = len(range_list)
    while len(range_list) > 0:
        (s, e) = range_list.pop(0)
        update_ranges(updated_ranges, s, e)
    range_list = updated_ranges

total_size = sum(b - a + 1 for a, b in range_list)
print("Fresh ingredients: ", total_size)