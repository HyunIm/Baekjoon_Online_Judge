M = int(input())
N = int(input())
i = 0
tmp = -1
answer_sum = 0
answer_min = 987654321

while tmp < N:
    tmp = i**2
    if M <= i**2 <= N:
        answer_min = min(tmp, answer_min)
        answer_sum += tmp
    i += 1

if answer_sum:
    print(answer_sum)
    print(answer_min)
else:
    print(-1)
