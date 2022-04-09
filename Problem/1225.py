A, B = input().split()
A = list(map(int, A))
B = list(map(int, B))
answer = 0

for i in A:
    for j in B:
        answer += i*j
print(answer)
