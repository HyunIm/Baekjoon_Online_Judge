T = int(input())
for _ in range(T):
    M, cn = input().split()
    data = input().split()
    if cn == 'C':
        for i in data:
            print(ord(i) - ord('A') + 1, end=' ')
    elif cn == 'N':
        for i in data:
            print(chr(int(i) + ord('A') - 1), end=' ')
    print()
