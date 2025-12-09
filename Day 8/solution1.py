import math

points = []
points_distances = []
highest_circuit = 0

def insertion_sort(points_distances):
    j = len(points_distances) - 2
    distance_tuple = points_distances[j + 1]
    distance = distance_tuple[0]
    while j >= 0 and points_distances[j][0] > distance:
        points_distances[j + 1] = points_distances[j]
        j -= 1
    points_distances[j + 1] = distance_tuple

with open("input8.txt", "r") as f:
    for line in f:
        line = line.strip()
        comma_split = line.split(",")
        x = int(comma_split[0])
        y = int(comma_split[1])
        z = int(comma_split[2])
        points.append([(x, y, z), 0])

half_points = len(points)
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        d = math.dist(points[i][0], points[j][0])
        points_distances.append((d, (i, j)))
        insertion_sort(points_distances)
        if len(points_distances) > half_points:
            points_distances.pop()

for distance_tuple in points_distances:
    closest_first = distance_tuple[1][0]
    closest_second = distance_tuple[1][1]

    circuit_first = points[closest_first][1]
    circuit_second = points[closest_second][1]
    if circuit_first == 0:
        if circuit_second == 0:
            highest_circuit += 1
            points[closest_first][1] = highest_circuit
            points[closest_second][1] = highest_circuit
        else:
            points[closest_first][1] = circuit_second
    else:
        if circuit_second == 0:
            points[closest_second][1] = circuit_first
        else:
            if circuit_first == circuit_second:
                continue
            if circuit_second < circuit_first:
                circuit_first, circuit_second = circuit_second, circuit_first
            for k in range(len(points)):
                if points[k][1] == circuit_second:
                    points[k][1] = circuit_first
            if circuit_second != highest_circuit:
                for k in range(len(points)):
                    if points[k][1] == highest_circuit:
                        points[k][1] = circuit_second
            highest_circuit -= 1

circuit_sizes = [0] * (highest_circuit + 1)
for p in points:
    circuit = p[1]
    if circuit > 0:
        circuit_sizes[circuit] += 1

largest = math.prod(sorted(circuit_sizes, reverse=True)[:3])
print("Three largest circuits: ", largest)