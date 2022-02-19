def flipCounter(S, flip):
    count = 0
    
    for i in range(len(S)):
        if S[i] == flip:
            if i == 0 or S[i-1] != S[i]:
                count += 1

    return count


S = input()
zeroFlip = flipCounter(S, '0')
oneFlip = flipCounter(S, '1')

print(min(zeroFlip, oneFlip))
