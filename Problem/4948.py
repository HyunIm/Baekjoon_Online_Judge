# File : 4948.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-11
# Brief : 수학

a = []
while n := int(input()): a.append(n)
big = max(a)*2
prime = [0, 0] + [1]*(big-1)
for i in range(2, big+1):
    if prime[i]:
        for j in range(2*i, big+1, i):
            prime[j] = 0
for i in a:
    print(sum(prime[i+1:2*i+1]))
