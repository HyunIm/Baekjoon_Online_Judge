msg = input()
len_msg = len(msg)
r = 0
c = 0

for i in range(1, len_msg + 1):
    tr = i
    tc = len_msg // tr
    if tr > tc:
        break
    if tr * tc == len_msg:
        r = tr
        c = tc

answer = []
for i in range(r):
    for j in range(c):
        answer.append(msg[i + j * r])
print(*answer, sep='')
