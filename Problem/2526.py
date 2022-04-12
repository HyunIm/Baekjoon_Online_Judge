N, P = map(int, input().split())
tmp = N
cycle = []
answer = 0

while not tmp in cycle:
    answer += 1
    cycle.append(tmp)
    tmp = tmp * N % P

print(answer - cycle.index(tmp))
