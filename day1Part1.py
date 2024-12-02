with open("inputs\inputDay1.txt") as file:
    data = file.read().splitlines()
arr1 = []
arr2 = []
res = 0

for line in data:
    l, r = line.split("   ")
    arr1.append(int(l))
    arr2.append(int(r))

arr1.sort()
arr2.sort()

for i in range(len(arr1)):
    res += abs(arr1[i]-arr2[i])
print(res)