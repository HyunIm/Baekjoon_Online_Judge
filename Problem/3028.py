data = input()
cup = [True, False, False]

for i in data:
    if i == 'A':
        cup[0], cup[1] = cup[1], cup[0]
    elif i == 'B':
        cup[1], cup[2] = cup[2], cup[1]
    elif i == 'C':
        cup[0], cup[2] = cup[2], cup[0]

for i in range(3):
    if cup[i] == True:
        print(i+1)
