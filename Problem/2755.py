m = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
     'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
     'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
     'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
     'F': 0.0}

N = int(input())
data = [list(input().split()) for _ in range(N)]
a = 0
sum_j = 0

for i, j, k in data:
    j = int(j)
    a += j * m[k]
    sum_j += j

print(round(a / sum_j + 0.0000001, 2))
