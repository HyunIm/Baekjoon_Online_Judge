N = int(input())
grade = list(map(int, input().split()))
score = 1 if grade[0] else 0
tmpScore = 1

for i in range(1, N):
    if grade[i]:
        if grade[i-1]:
            tmpScore += 1
            score += tmpScore
        else:
            tmpScore = 1
            score += tmpScore

print(score)
