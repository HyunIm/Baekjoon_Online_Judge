C, K, P = map(int, input().split())
wine = 0

for n in range(1, C+1):
    wine += K*n + P*(n**2)

print(wine)
