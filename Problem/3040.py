def find_false_dwarf(dwarf):
    sum_dwarf = sum(dwarf)

    for i in range(8):
        for j in range(i+1, 9):
            if sum_dwarf - (dwarf[i] + dwarf[j]) == 100:
                return i, j

dwarf = [int(input()) for _ in range(9)]

i, j = find_false_dwarf(dwarf)
del dwarf[j]
del dwarf[i]

for i in dwarf:
    print(i)
