points = []

def get_limit(right_point):
    global points
    right_point_x = right_point[0]
    for i in range(len(points) - 1, 0, -1):
        if points[i][0] < right_point_x:
            return points[i][1]
            
def find_largest_area(upper_half, right_point, limit):
    global points
    area = 0
    half_points = len(points) // 2
    right_x = right_point[0]
    right_y = right_point[1]
    for i in range(1, half_points):
        left_x = points[i][0]
        left_y = points[i][1]
        reaches_bottom = True
        if upper_half:
            for j in range(i - 1, 0, -1):
                y = points[j][1]
                if y > limit:
                    reaches_bottom = False
                    break
                x = points[j][0]
                if x > left_x:
                    reaches_bottom = False
        else:
            for j in range(i - 1, 0, -1):
                y = points[j][1]
                if y < limit:
                    reaches_bottom = False
                    break
                x = points[j][0]
                if x > left_x:
                    reaches_bottom = False
        if reaches_bottom:
            x_len = abs(left_x - right_x) + 1
            y_len = abs(left_y - right_y) + 1
            new_area = x_len * y_len
            if new_area > area:
                print("(", left_x, left_y, ",", right_x, right_y, ")")
                area = new_area
    return area

largest_area = 0
with open("input9.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        comma_split = line.split(",")
        x = int(comma_split[0])
        y = int(comma_split[1])
        points.append((x, y))
    points.reverse()
    right_point = points.pop()
    limit = get_limit(right_point)
    largest_area = find_largest_area(True, right_point, limit)
    points = []
    for line in f:
        line = line.strip()
        comma_split = line.split(",")
        x = int(comma_split[0])
        y = int(comma_split[1])
        points.append((x, y))
    right_point = points.pop()
    limit = get_limit(right_point)
    second_area = find_largest_area(False, right_point, limit)
    largest_area = max(second_area, largest_area)

print("The largest rectangle: ", largest_area)