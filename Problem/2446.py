N = int(input())

for i in range(N):
    print(' '*i + '*'*(N-i-1)*2 + '*')
for i in range(1, N):
    print(' '*(N-i-1) + '*'*i*2 + '*')
