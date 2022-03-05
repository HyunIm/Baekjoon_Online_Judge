n = int(input())

cyScore = 100
sdScore = 100

for _ in range(n):
    cy, sd = map(int, input().split())
    if cy < sd:
        cyScore -= sd
    elif cy > sd:
        sdScore -= cy
    elif cy == sd:
        pass

print(cyScore)
print(sdScore)
