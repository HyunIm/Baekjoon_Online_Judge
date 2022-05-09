m = {'c' : 26, 'd' : 10}

data = input()
answer = m[data[0]]

for i in range(1, len(data)):
    if data[i] == data[i - 1]:
        answer *= (m[data[i]] - 1)
    else:
        answer *= m[data[i]]
print(answer)
