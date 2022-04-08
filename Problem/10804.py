card = [i for i in range(1, 21)]

for _ in range(10):
    x, y = map(int, input().split())
    card = card[:x-1] + list(reversed(card[x-1:y])) + card[y:]

print(*card)
