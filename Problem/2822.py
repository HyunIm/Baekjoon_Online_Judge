data = []
for i in range(1, 9):
    data.append((int(input()), i))
answer = sorted(data, reverse=True)[:5]
sum_value = sum([i[0] for i in answer])
idx_value = sorted([i[1] for i in answer])

print(sum_value)
print(*idx_value)
