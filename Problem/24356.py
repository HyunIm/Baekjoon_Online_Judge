t1, m1, t2, m2 = map(int, input().split())

time1 = t1*60 + m1
time2 = t2*60 + m2

totalTime = time2 - time1
if totalTime < 0:
    totalTime += 24*60

print(totalTime, totalTime//30)
