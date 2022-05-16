A, B = map(int, input().split())
seq = []
answer = 0
for i in range(1, B + 1):
    for j in range(i):
        seq.append(i)
answer = sum(seq[A-1:B])
print(answer)
