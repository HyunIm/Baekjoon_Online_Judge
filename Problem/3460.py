T = int(input())

for _ in range(T):
    n = int(input())
    n = bin(n)[2:][::-1]

    for i in range(len(n)):
        if n[i] == '1':
            print(i, end=' ')
    print()
