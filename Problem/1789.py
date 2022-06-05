N = int(input())
tmp = 1
answer = -1

while N >= 0:
    N -= tmp
    tmp += 1
    answer += 1

print(answer)
