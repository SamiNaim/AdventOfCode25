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

# 515617267 too low
# 637914408 too low
# 1618518804 too high
# 1613305596

"""

        for j in range(len(points) - 1, half_points, -1):
            i_x = points[i][0]
            i_y = points[i][1]
            j_x = points[j][0]
            j_y = points[j][1]
            if i_x == j_x or i_y == j_y:
                continue
            i_is_lower = True
            if i_y > j_y:
                i_is_lower = False
            left_fit = False
            right_fit = False
            if i_is_lower:
                if upper_half:
                    counter = i
                    
                for ii in range(half_points):
                    if ii == i:
                        continue
                    x = points[ii][0]
                    y = points[ii][1]
                    if x <= i_x and y >= j_y:
                        left_fit = True
                for jj in range(len(points) - 1, half_points, -1):
                    if jj == j:
                        continue
                    x = points[jj][0]
                    y = points[jj][1]
                    if x >= j_x and y <= i_y:
                        right_fit = True
            else:
                for ii in range(half_points):
                    if ii == i:
                        continue
                    x = points[ii][0]
                    y = points[ii][1]
                    if x <= i_x and y <= j_y:
                        left_fit = True
                for jj in range(len(points) - 1, half_points, -1):
                    if jj == j:
                        continue
                    x = points[jj][0]
                    y = points[jj][1]
                    if x >= j_x and y >= i_y:
                        right_fit = True
            if left_fit and right_fit:
                x_len = abs(i_x - j_x) + 1
                y_len = abs(i_y - j_y) + 1
                new_area = x_len * y_len
                if new_area > area:
                    print("(", i_x, i_y, ",", j_x, j_y, ")")
                    area = new_area
"""