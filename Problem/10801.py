A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_score = 0
b_score = 0

for i in range(10):
    if A[i] > B[i]:
        a_score += 1
    elif A[i] < B[i]:
        b_score += 1

if a_score == b_score:
    print('D')
elif a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
