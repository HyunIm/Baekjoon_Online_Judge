N = int(input())

idx = 10
while N > idx:
    tmp = N % idx
    if tmp >= idx // 2:
        N += idx
    N -= tmp
    idx *= 10

print(N)
