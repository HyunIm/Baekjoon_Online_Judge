N, M, L = map(int, input().split())
answer = -1
count = [0] * N
now = 0

while max(count) < M:
    answer += 1
    count[now] += 1
    if count[now] % 2:
        now = now+L if now+L < N else (now+L)-N
    else:
        now = now-L if now-L >= 0 else (now-L)+N
print(answer)
