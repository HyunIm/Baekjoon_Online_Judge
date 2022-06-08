N = int(input())
ns = set(map(int, input().split()))
M = int(input())
ms = list(map(int ,input().split()))

for i in ms:
    print(1 if i in ns else 0, end=' ')
