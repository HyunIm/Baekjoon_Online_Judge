song = ['baby', 'sukhwan', 'tururu', 'turu',
        'very', 'cute', 'tururu', 'turu',
        'in', 'bed', 'tururu', 'turu',
        'baby', 'sukhwan']

N = int(input()) - 1
cnt = N // 14
loc = N % 14

if loc in [2, 6, 10]:
    if cnt >= 3:
        print('tu+ru*', cnt+2, sep='')
    else:
        print('tururu' + 'ru'*cnt)
elif loc in [3, 7, 11]:
    if cnt >= 4:
        print('tu+ru*', cnt+1, sep='')
    else:
        print('turu' + 'ru'*cnt)
else:
    print(song[loc])
