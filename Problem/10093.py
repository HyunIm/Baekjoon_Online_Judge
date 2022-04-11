A, B = sorted(map(int, input().split()))
print(B-A-1 if B-A-1 >= 0 else 0)
for i in range(A+1, B):
    print(i, end=' ')
