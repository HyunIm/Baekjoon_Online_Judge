data = input().upper()
vowel = ['A', 'E', 'I', 'O', 'U']

while data != '#':
    answer = 0
    for i in vowel:
        answer += data.count(i)
    print(answer)
    data = input().upper()
