N = int(input())
data = list(set(list(map(int, input().split()))))
data.sort()
print(*data)
