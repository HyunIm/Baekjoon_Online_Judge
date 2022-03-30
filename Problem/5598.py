word = input()

for i in word:
    if 'D' <= i <= 'Z':
        tmp = chr(ord(i)-3)
    else:
        tmp = chr(ord(i)-3+26)
    print(tmp, end='')
