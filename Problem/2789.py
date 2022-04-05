word = input()
block = ('C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E')

for i in word:
    if i in block:
        continue
    print(i, end='')
