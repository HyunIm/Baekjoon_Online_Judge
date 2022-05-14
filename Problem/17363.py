trun = {'.' : '.', 'O' : 'O', '-' : '|', '|' : '-', '/' : '\\',
        '\\' : '/', '^' : '<', '<' : 'v', 'v' : '>', '>' : '^'}

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
for i in range(M-1, -1, -1):
    for j in range(N):
        print(trun[data[j][i]], end='')
    print()
