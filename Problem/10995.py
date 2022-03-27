N = int(input())

for i in range(N):
    if i%2:
        for j in range(N*2):
            print('*' if j%2 else ' ', end='')
    else:
        for j in range(N*2):
            print(' ' if j%2 else '*', end='')
    print()
