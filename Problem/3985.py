L = int(input())
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
cake = [0] * (L + 1)

diff = [j-i for i, j in data]
max_hope = diff.index(max(diff)) + 1

for idx in range(N):
    i, j = data[idx]
    for k in range(i, j+1):
        if cake[k] == 0:
            cake[k] = idx + 1

max_real = 0
max_real_cnt = 0
for i in range(1, N + 1):
    cake_cnt = cake.count(i)
    if cake_cnt > max_real_cnt:
        max_real = i
        max_real_cnt = cake_cnt

print(max_hope)
print(max_real)
