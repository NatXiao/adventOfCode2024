with open("inputs\inputDay.txt") as file:
    data = file.read().splitlines()

def testPath(guardPos, tab):
    out = False
    currentDirection = 0
    direction = [(-1, 0), (0, 1),(1, 0), (0, -1)]
    positionAlreadyPassed =[]
    directionTaken = []
    positionAlreadyPassed.append(guardPos)
    directionTaken.append(currentDirection)
    while(not out):
        dy, dx = direction[currentDirection]
        dy += guardPos[0]
        dx += guardPos[1]
        if dy >= len(tab) or dx >= len(tab[0]) or dy < 0 or dx <  0:
            out = True
        elif tab[dy][dx] == '#':
            currentDirection = (currentDirection+1) % 4

        else :
            guardPos = (dy, dx)
            if guardPos in positionAlreadyPassed:
                if currentDirection == directionTaken[positionAlreadyPassed.index(guardPos)]:
                    print("this is a loop")
                    #loop
                    return True
                    break
                else :
                    continue
            else :
                positionAlreadyPassed.append(guardPos)
                directionTaken.append(currentDirection)
    return False


guardPos = (0,0)
res = 0

tableau = []

for i, lines in enumerate(data):
    tableau.append(list(lines))
    for char in lines:
        if char == '^':
            guardPos = (i, data[i].index('^'))
            break

for y, line in enumerate(data):
    for x in range(len(lines)):
        if tableau[y][x]== '^' or tableau[y][x] == '#':
            continue
        tableau[y][x] = '#'
        if testPath(guardPos, tableau) :
            res += 1
            print(res)
        tableau[y][x] = '.'
print(res)



