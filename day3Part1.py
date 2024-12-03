import re
with open("inputs\inputDay3.txt") as file:
    data = file.read().splitlines()

res = 0

for line in data:
    #detect mul() pattern
    mulThing = [s for s in re.findall(r'mul\(\d+,\d+\)', line)]
    for detected in mulThing:
        val1, val2= detected[4:-1].split(",")
        print(val1, val2)
        res += int(val1)*int(val2)
print(res)










