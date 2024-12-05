with open("inputs\inputDay4.txt") as file:
    data = file.read().splitlines()
res = 0
tab = []

for line in data:
    tab.append(line)
    
for y in range(len(tab)):
    for x in range(len(tab[0])): #parcourt le tableau
        if tab[y][x] == 'X': #trouve le x
            for dy in range(-1,2): #parcourt chaque direction
                for dx in range(-1, 2):
                    if (y+3*dy) >= 0 and (y+3*dy)< len(tab) and (x+3*dx)<len(tab[0]) and (x+3*dx) >=0:
                        if tab[y+dy][x+dx] == 'M' and tab[y+2*dy][x+2*dx] == 'A' and tab[y+3*dy][x+3*dx] == 'S':
                            res += 1
print(res)