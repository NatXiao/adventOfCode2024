with open("inputs\inputDay.txt") as file:
    data = file.read().splitlines()
res = 1

currentDirection = 0
direction = [(-1, 0), (0, 1),(1, 0), (0, -1)]
guardPos = (0,0)
positionAlreadyPassed =[]
out = False

for i, lines in enumerate(data):
    for char in lines:
        if char == '^':
            guardPos = (i, data[i].index('^'))
            break
positionAlreadyPassed.append(guardPos)
while(not out):
    dy, dx = direction[currentDirection]
    dy += guardPos[0]
    dx += guardPos[1]
    if dy >= len(data) or dx >= len(data[0]) or dy < 0 or dx <  0:
        out = True
    elif data[dy][dx] == '#':
        currentDirection = (currentDirection+1) % 4

    else :
        guardPos = (dy, dx)
        if guardPos in positionAlreadyPassed :
            continue
        else :
            positionAlreadyPassed.append(guardPos)
            res += 1

print(res)