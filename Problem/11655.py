S = input()
for i in S:
    if i.isalpha():
        tmp = ord(i) + 13
        if 'a' <= i <= 'z':
            if tmp > ord('z'):
                tmp -= 26
        else:
            if tmp > ord('Z'):
                tmp -= 26
        print(chr(tmp), end='')
    else:
        print(i, end='')
