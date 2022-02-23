N = int(input())
extraApple = 0

for _ in range(N):
    student, apple = map(int, input().split())
    extraApple += apple % student

print(extraApple)
