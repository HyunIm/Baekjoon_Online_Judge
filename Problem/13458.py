N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for student in A:
    student -= B
    result += 1
    if student > 0:
        result += (student//C+1) if student%C else student//C

print(result)
