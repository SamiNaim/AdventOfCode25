points = []

with open("input9.txt", "r") as f:
    for line in f:
        line = line.strip()
        comma_split = line.split(",")
        x = int(comma_split[0])
        y = int(comma_split[1])
        points.append((x, y))

area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        i_x = points[i][0]
        i_y = points[i][1]
        j_x = points[j][0]
        j_y = points[j][1]
        x_len = abs(i_x - j_x) + 1
        y_len = abs(i_y - j_y) + 1
        new_area = x_len * y_len
        if new_area > area:
            area = new_area

print("The largest rectangle: ", area)