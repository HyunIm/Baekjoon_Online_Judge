# File : 18406.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-12
# Brief : 구현

n = list(map(int, input()))
l = int(len(n)/2)
print('LUCKY' if sum(n[:l])==sum(n[l:]) else 'READY')
