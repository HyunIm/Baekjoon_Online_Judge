# File : 1439.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-05-23
# Brief : 그리디 알고리즘

s = input()
zero = 0
one = 0

if (s[0] == '0'):
    one += 1
else:
    zero += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '0':
            one += 1
        else:
            zero += 1

print(min(zero, one))
