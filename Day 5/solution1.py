fresh = 0

with open("input5.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break

    for line in f:
        line = line.strip()
        ingredient_id = int(line)
        spoiled = True
        with open("input5.txt", "r") as ff:
            for line in ff:
                line = line.strip()
                if line == "":
                    break
                dash_split = line.split("-")
                start_id = int(dash_split[0])
                end_id = int(dash_split[1])
                if ingredient_id >= start_id and ingredient_id <= end_id:
                    spoiled = False
                    break

        if not spoiled:
            fresh += 1

print("Fresh ingredients: ", fresh)