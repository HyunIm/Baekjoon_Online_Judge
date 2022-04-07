N = int(input())
bar = [int(input()) for _ in range(N)]
answer = 0

bar.reverse()
now = 0
for i in bar:
    if i > now:
        answer += 1
        now = i
print(answer)
