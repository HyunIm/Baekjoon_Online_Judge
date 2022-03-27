N = int(input())
players = [input() for _ in range(N)]
result = [0]*26

for player in players:
    index = ord(player[0]) - ord('a')
    result[index] += 1

flag = False
for i in range(26):
    if result[i] >= 5:
        print(chr(i + ord('a')), end='')
        flag = True
if flag == False:
    print('PREDAJA')
