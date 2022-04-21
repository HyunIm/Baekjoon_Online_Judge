N = int(input())
files = list(map(int, input().split()))
cluster = int(input())
answer = 0

for i in files:
    tmp = i//cluster+1 if i/cluster != i//cluster else i//cluster
    answer += tmp * cluster

print(answer)
