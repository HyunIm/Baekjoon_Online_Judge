N = int(input())
students = list(map(int, input().split()))

print(max(students) - min(students))
