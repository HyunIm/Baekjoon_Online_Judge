t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    answer = (max(x) - min(x)) * 2
    print(answer)
