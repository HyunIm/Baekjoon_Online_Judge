N = int(input())
student = list(map(int, input().split()))
hit = 0

for i in range(N):
    if i+1 != student[i]:
        hit += 1

print(hit)
