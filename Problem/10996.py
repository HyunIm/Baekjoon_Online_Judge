N = int(input())

for _ in range(N):
    for i in range(N):
        print(' ' if i%2 else '*', end='')
    print()
    for j in range(N):
        print('*' if j%2 else ' ', end='')
    print()
