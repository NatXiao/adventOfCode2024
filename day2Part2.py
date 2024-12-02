with open("inputs\inputDay2.txt") as file:
    data = file.read().splitlines()

res = 0

def isValid(report):
    increasing = True
    decreasing = True
    correctSteps = True
    for i in range(len(report)-1):
        level = int(report[i])
        level1 = int(report[i+1])
        if level > level1 : #decreasing
            increasing = False
        elif level < level1:
            decreasing = False
        else:
            increasing = False
            decreasing = False
            break
        if abs(level-level1)>3 or abs(level-level1)<1:
            correctSteps = False
            break
    return (increasing or decreasing) and correctSteps
        
    

for line in data:
    report = line.split(" ")
    for i in range(len(report)):
        if isValid(report[:i]+report[i+1:]):
            res+=1
            break
print(res)





