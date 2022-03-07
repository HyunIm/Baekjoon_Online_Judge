T = int(input())

for _ in range(T):
    
    N = int(input())
    totalC = 0
    GPA = 0
    for _ in range(N):
        C, G = map(float, input().split())
        totalC += C
        GPA += G * C
    print(int(totalC), '%.1f'%GPA / totalC)
