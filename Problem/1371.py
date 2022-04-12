import sys

data = sys.stdin.read()
count = [0] * 26

for i in data:
    if 'a' <= i <= 'z':
        count[ord(i) - ord('a')] += 1

max_value = max(count)
for i in range(26):
    if count[i] == max_value:
        print(chr(i + ord('a')), end='')
