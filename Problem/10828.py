import sys
input = sys.stdin.readline

N = int(input())
s = []

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        s.append(cmd[1])
    elif cmd[0] == 'pop':
        print(s.pop() if s else -1)
    elif cmd[0] == 'size':
        print(len(s))
    elif cmd[0] == 'empty':
        print(0 if s else 1)
    elif cmd[0] == 'top':
        print(s[-1] if s else -1)
