n = int(input())
data = [list(input().split()) for _ in range(n)]
data.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
print(data[-1][0])
print(data[0][0])
