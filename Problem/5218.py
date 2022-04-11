T = int(input())

for _ in range(T):
    x, y = input().split()
    print('Distances: ', end='')
    for i in range(len(x)):
        gap = ord(y[i]) - ord(x[i])
        gap = gap if gap >= 0 else 26+gap
        print(gap, end=' ')
    print()
