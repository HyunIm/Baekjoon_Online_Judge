N = int(input())

for i in range(N):
    print(' '*(N-i-1) + '*' + '*'*(i*2))
for i in range(1, N):
    print(' '*i + '*' + '*'*((N-i-1)*2))
