import sys

input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    line = list(input().split())
    cmd = line[0]
    x = int(line[1]) if len(line) == 2 else 0

    if cmd == 'add':
        S.add(x)

    elif cmd == 'remove':
        S.discard(x)

    elif cmd == 'check':
        print(1 if x in S else 0)

    elif cmd == 'toggle':
        S.remove(x) if x in S else S.add(x)

    elif cmd == 'all':
        S = set([i for i in range(1, 21)])

    elif cmd == 'empty':
        S = set()
