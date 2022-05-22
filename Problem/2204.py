n = int(input())
while n != 0:
    data = [input() for _ in range(n)]
    data.sort(key=lambda x: x.lower())
    print(data[0])
    n = int(input())
