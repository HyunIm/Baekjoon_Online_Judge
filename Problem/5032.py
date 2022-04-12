e, f, c = map(int, input().split())
answer = 0

e += f
while e >= c:
    answer += e//c
    tmp = e//c
    e %= c
    e += tmp

print(answer)
