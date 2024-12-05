with open("inputs\inputDay5.txt") as file:
    data = file.read().splitlines()
res = 0

#split my data
ruleEnded = False
rule = []
listToCheck = []

for l in data :
    if l == '':
        ruleEnded = True
    elif ruleEnded:
        listToCheck.append(l)
    else :
        rule.append(l)

rules = dict()

for n in rule :
    l, r = n.split("|")
    if not int(l) in rules:
        rules[int(l)] = []
    rules[int(l)].append(int(r))

for line in listToCheck :
    valid = True
    numbers = list(map(int, line.split(',')))
    for i, n in enumerate(numbers):
        if n not in rules:
            print(n)
            continue
        for r in rules[n]:
            if r in numbers[0:i]:
                valid = False
                break
    if valid :
        print(numbers)
        res += numbers[len(numbers)//2]
            
print(res)