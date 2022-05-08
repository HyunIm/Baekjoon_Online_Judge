N = int(input())
for i in range(1, N + 1):
    L = input().split()
    print('Case #', i, ': ', sep='', end='')
    print(*L[::-1])
