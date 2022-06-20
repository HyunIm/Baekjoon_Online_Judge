import sys
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
data.sort(reverse=True)
print(*data, sep='\n')
