N = int(input())
answer = input()
length = len(answer)
for _ in range(N - 1):
    data = input()
    for i in range(length):
        if answer[i] != data[i]:
            answer = answer[:i] + '?' + answer[i+1:]
print(answer)
