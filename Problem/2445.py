N = int(input())

for i in range(N):
    print('*' + '*'*i + ' '*(N-i-1)*2 + '*'*i + '*')
for i in range(N-1):
    print('*' + '*'*(N-i-2) + ' '*(i+1)*2 + '*'*(N-i-2) + '*')
