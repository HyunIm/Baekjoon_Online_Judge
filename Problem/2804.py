def find_cross_location(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return i, j


A, B = input().split()

x, y = find_cross_location(A, B)

for i in range(len(B)):
    for j in range(len(A)):
        if i == y:
            print(A, end='')
            break
        elif j == x:
            print(B[i], end='')
        else:
            print('.', end='')
    print()
