data1 = list(input())
data2 = list(input())
answer = 0

while data1 or data2:
    if data1:
        if data1[0] in data2:
            data2.remove(data1[0])
            data1.remove(data1[0])
        else:
            data1.remove(data1[0])
            answer += 1

    if data2:
        if data2[0] in data1:
            data1.remove(data2[0])
            data2.remove(data2[0])
        else:
            data2.remove(data2[0])
            answer += 1

print(answer)
