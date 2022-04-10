def can_room_assignments(a, b, c, n):
    for i in range(0, n+1, a):
        for j in range(0, n+1, b):
            for k in range(0, n+1, c):
                if i+j+k == n:
                    return 1
    return 0


A, B, C, N = map(int, input().split())
print(can_room_assignments(A, B, C, N))
