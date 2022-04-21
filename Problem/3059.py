T = int(input())
for _ in range(T):
    S = input()
    alphabet = [False] * 26
    answer = 0
    for i in S:
        index = ord(i) - ord('A')
        alphabet[index] = True
    for i in range(26):
        if alphabet[i] == False:
            answer += (i+65)
    print(answer)
