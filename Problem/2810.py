N = int(input())
data = input()
answer = 1

for i in data:
    if i == 'S':
        answer += 1
    elif i == 'L':
        answer += 0.5
print(min(int(answer), N))
