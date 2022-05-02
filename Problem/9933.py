N = int(input())
data = [input() for _ in range(N)]

for i in range(N):
    for j in range(i, N):
        if data[i] == data[j][::-1]:
            len_data = len(data[i])
            print(len_data, data[i][len_data // 2])
