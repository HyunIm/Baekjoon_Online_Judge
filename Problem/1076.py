color = { 'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4,
         'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9 }

resistance_color = [color[input()] for _ in range(3)]
resistance_value = 0

resistance_value = int(str(resistance_color[0]) + str(resistance_color[1]))
resistance_value *= 10**resistance_color[2]

print(resistance_value)
