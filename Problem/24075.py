A, B = map(int, input().split())

ApB, AmB = A+B, A-B

print(max(ApB, AmB))
print(min(ApB, AmB))
