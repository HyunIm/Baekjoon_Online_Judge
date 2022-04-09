N = int(input())

for _ in range(N):
    data = input()
    data = data[0].upper() + data[1:]
    print(data)
