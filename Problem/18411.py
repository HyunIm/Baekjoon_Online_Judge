A, B, C = map(int, input().split())

grade = [A, B, C]

print(sum(grade) - min(grade))
