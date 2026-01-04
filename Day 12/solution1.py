shapes_areas = []
regions = []

with open("input12.txt", "r") as f:
    idx = 0
    area = 0
    shape = 0
    for line in f:
        line = line.strip()
        if shape > 0:
            area += line.count("#")
            print(line)
            print(area)
            shape -= 1
            if shape == 0:
                shapes_areas.append(area)
                area = 0
        if ':' in line and 'x' not in line:
            idx = int(line.rstrip(':'))
            shape = 3
        elif 'x' in line:
            parts = line.split(':')
            dims = parts[0].split('x')
            width, height = int(dims[0]), int(dims[1])
            counts = list(map(int, parts[1].split()))
            regions.append((width, height, counts))
    
count = 0
for width, height, counts in regions:
    tight_area = 0
    for i, c in enumerate(counts):
        tight_area += (shapes_areas[i] * c)
    if width * height >= tight_area:
        count += 1
    print(width * height, tight_area)

print(count, "of the regions can fit all of the presents listed")