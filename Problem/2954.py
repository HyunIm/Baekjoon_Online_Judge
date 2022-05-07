data = input()
answer = ''
i = 0

while i != len(data):
    answer += data[i]
    if data[i] in ('a', 'e', 'i', 'o', 'u'):
        i += 2
    i += 1
print(answer)
