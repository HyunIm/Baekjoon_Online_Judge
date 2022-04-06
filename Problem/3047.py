A, B, C = sorted(map(int, input().split()))
order = input()

for i in order:
    if i == 'A':
        print(A, end=' ')
    elif i == 'B':
        print(B, end=' ')
    elif i == 'C':
        print(C, end=' ')
