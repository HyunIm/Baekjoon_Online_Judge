N = int(input())
data = list(map(int, input().split()))
computer = [False] * 101
answer = 0

for i in data:
    if computer[i] == True:
        answer += 1
    else:
        computer[i] = True

print(answer)
