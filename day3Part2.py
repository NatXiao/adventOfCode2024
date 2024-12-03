import re
with open("inputs\inputDay3.txt") as file:
    data = file.read().splitlines()

res = 0
enable = True

for line in data:
    #detect mul() pattern
    mulThing = [s for s in re.findall(r'do\(\)|mul\(\d+,\d+\)|don\'t\(\)', line)]
    print(mulThing)
    for detected in mulThing:
        if detected == "don't()":
            enable = False
        elif detected == "do()":
            enable = True
        else:
            if enable :
                val1, val2= detected[4:-1].split(",")
                print(val1, val2)
                res += int(val1)*int(val2)
print(res)










