def is_cracker(i, data):
    for j in data:
        if i%j == 0:
            return True
    return False


N, C = map(int, input().split())
data = [int(input()) for _ in range(N)]
answer = 0

for i in range(1, C+1):
    if is_cracker(i, data):
        answer += 1
print(answer)
