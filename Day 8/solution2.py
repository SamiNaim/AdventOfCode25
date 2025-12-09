import math

points = []

def insertion_sort(points_distances):
    j = len(points_distances) - 2
    distance_tuple = points_distances[j + 1]
    distance = distance_tuple[0]
    while j >= 0 and points_distances[j][0] > distance:
        points_distances[j + 1] = points_distances[j]
        j -= 1
    points_distances[j + 1] = distance_tuple

def condition(points_to_sort):
    global points
    connected_points = set()
    points_distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = math.dist(points[i], points[j])
            points_distances.append((d, (i, j)))
            insertion_sort(points_distances)
            if len(points_distances) > points_to_sort:
                points_distances.pop()
    for distance_tuple in points_distances:
        closest_first = distance_tuple[1][0]
        closest_second = distance_tuple[1][1]
        connected_points.add(closest_first)
        connected_points.add(closest_second)
    return closest_first, closest_second, len(connected_points) == len(points)

with open("input8.txt", "r") as f:
    for line in f:
        line = line.strip()
        comma_split = line.split(",")
        x = int(comma_split[0])
        y = int(comma_split[1])
        z = int(comma_split[2])
        points.append((x, y, z))

points_to_sort = len(points)
b = False
while True:
    _, _, b = condition(points_to_sort)
    if b:
        break
    points_to_sort *= 2

print("done", points_to_sort)

lo = points_to_sort // 2
hi = points_to_sort

while lo + 1 < hi:
    mid = (lo + hi) // 2
    i, j, b = condition(mid)
    print(mid, b)
    if b:
        hi = mid
    else:
        lo = mid

i, j, b = condition(hi)
print("Two last junction boxes: ", points[i][0] * points[j][0])