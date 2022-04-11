data = input()
joi = 0
ioi = 0

for i in range(2, len(data)):
    if data[i] == 'I':
        if data[i-2:i] == 'JO':
            joi += 1
        elif data[i-2:i] == 'IO':
            ioi += 1
            
print(joi)
print(ioi)
