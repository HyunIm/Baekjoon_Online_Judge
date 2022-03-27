import sys

m = {1:1, }

def triangular_number_calc():
    for i in range(1001):
        m[i] = i*(i+1)//2


def triangular_number_sum(k):
    for a in range(1, k):
        for b in range(a, k):
            for c in range(b, k):
                if k == m[a] + m[b] + m[c]:
                    return 1
    return 0


T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    triangular_number_calc()
    print(triangular_number_sum(K))
