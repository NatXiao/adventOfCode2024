with open("inputs\inputDay4.txt") as file:
    data = file.read().splitlines()
res = 0
tab = []


for line in data:
    tab.append(line)
    
for y in range(1, len(tab)-1):
    for x in range(1, len(tab[0])-1): #parcourt le tableau
        if tab[y][x] == 'A': #trouve le A
            if tab[y-1][x-1] == 'M' and tab[y+1][x-1] == 'M' and tab[y-1][x+1] == 'S' and tab[y+1][x+1]== 'S':
                res += 1
            if tab[y-1][x-1] == 'M' and tab[y+1][x-1] == 'S' and tab[y-1][x+1] == 'M' and tab[y+1][x+1]== 'S':
                res += 1
            if tab[y-1][x-1] == 'S' and tab[y+1][x-1] == 'S' and tab[y-1][x+1] == 'M' and tab[y+1][x+1]== 'M':
                res += 1
            if tab[y-1][x-1] == 'S' and tab[y+1][x-1] == 'M' and tab[y-1][x+1] == 'S' and tab[y+1][x+1]== 'M':
                res += 1
print(res)