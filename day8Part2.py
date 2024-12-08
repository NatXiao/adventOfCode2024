with open("inputs\inputDay8.txt") as file:
    data = file.read().splitlines()
res =0
letterPos = {}
found = set()

for y in range(len(data)):
    for x in range(len(data[y])):
        char = data[y][x]
        if char != '.':
            if char not in letterPos:
                letterPos[char] = []
            letterPos[char].append((y, x))

for poses in letterPos.values():
    if len(poses) == 1:
        continue
    for i in range(len(poses)):
        for i2 in range(i+1, len(poses)):
            dx = poses[i][0] - poses[i2][0]
            dy = poses[i][1] - poses[i2][1]
            mul = 0
            while len(data[0])>poses[i][0] + mul* dx >= 0 and len(data) > poses[i][1] +mul* dy >=0:
                found.add((poses[i][0] + mul *dx, poses[i][1] + mul *dy ))
                mul += 1
            mul = 0
            while len(data[0])>poses[i2][0] - mul*dx >= 0 and len(data) > poses[i2][1] - mul * dy >=0:
                found.add((poses[i2][0] - mul *dx, poses[i2][1] - mul *dy ))
                mul +=1


print(len(found))