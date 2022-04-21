def count_view(data, N):
    answer = 1
    height = data[0]
    for i in range(N-1):
        if height == data[i+1]:
            continue
        elif height < data[i+1]:
            height = data[i+1]
            answer += 1
    return answer


N = int(input())
data = [int(input()) for _ in range(N)]

left_answer = count_view(data, N)
right_answer = count_view(list(reversed(data)), N)
print(left_answer)
print(right_answer)
