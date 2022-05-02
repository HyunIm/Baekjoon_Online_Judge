def get_winner(A, B):
    for i in range(4, 0, -1):
        if A.count(i) > B.count(i):
            return 'A'
        elif A.count(i) < B.count(i):
            return 'B'
    return 'D'


N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(get_winner(A[1:], B[1:]))
