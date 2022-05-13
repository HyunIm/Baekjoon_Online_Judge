R, C = map(int, input().split())
data = [list(input()) for _ in range(R)]
A, B = map(int, input().split())

for i in range(R):
    data[i] = data[i] + data[i][::-1]

for i in data[::-1]:
    data.append(list(i))

data[A-1][B-1] = '.' if data[A-1][B-1] == '#' else '#'

for i in data:
    print(*i, sep='')
