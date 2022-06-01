import math

f = math.factorial

N = int(input())
answer = 0

for i in str(f(N))[::-1]:
    if i == '0':
        answer += 1
    else:
        break

print(answer)
