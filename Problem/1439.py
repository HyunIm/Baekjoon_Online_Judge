# File : 11-3.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-18
# Brief : 그리디

s = input()
f = s[0]
a = int(s[0])
b = 0 if int(s[0]) else 1
for i in range(1, len(s)):
    if f=='0' and s[i]=='1':
        a += 1
    elif f=='1' and s[i]=='0':
        b += 1
    f = s[i]
print(min(a, b))
