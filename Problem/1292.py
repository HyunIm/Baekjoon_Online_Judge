A, B = map(int, input().split())
data = []
tmp = 1
end = 0

while B > end:
    for _ in range(tmp):
        data.append(tmp)
    end += tmp
    tmp += 1

print(sum(data[A-1:B]))
