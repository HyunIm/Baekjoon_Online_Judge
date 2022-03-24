def findFalseDwarf(dwarf):
    sumDwarf = sum(dwarf)
    for i in range(9):
        for j in range(i+1, 9):
            if sumDwarf - (dwarf[i] + dwarf[j]) == 100:
                return i, j


dwarf = sorted([int(input()) for _ in range(9)])

i, j = findFalseDwarf(dwarf)
del dwarf[j]
del dwarf[i]

for i in dwarf:
    print(i)
