T = int(input())
for _ in range(T):
    N = int(input())
    S = [list(input().split()) for _ in range(N)]
    S = sorted(S, key=lambda x : -int(x[1]))
    print(S[0][0])
