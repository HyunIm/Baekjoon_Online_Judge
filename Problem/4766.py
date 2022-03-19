temperature = float(input())

while True:
    preTemperature = temperature
    temperature = float(input())

    if temperature == 999:
        break
    
    print('%.2f'%(temperature - preTemperature))
