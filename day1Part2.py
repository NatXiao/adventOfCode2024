from collections import Counter

with open("inputs\inputDay1.txt") as file:
    data = file.read().splitlines()
arr1 = []
arr2 = []
res = 0

for line in data:
    l, r = line.split("   ")
    arr1.append(int(l))
    arr2.append(int(r))

count = Counter(arr2)
print(count)

for i in arr1:
    res += i*count[i]
print(res)