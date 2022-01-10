startTime = input()
endTime = input()

startHour, startMinute, startSecond = map(int, startTime.split(':'))
endHour, endMinute, endSecond = map(int, endTime.split(':'))

totalStartTime = 3600*startHour + 60*startMinute + startSecond
totalEndTime = 3600*endHour + 60*endMinute + endSecond

betweenTimes = totalEndTime - totalStartTime

if totalStartTime < totalEndTime:
    print(betweenTimes)
else:
    print(betweenTimes + 24*3600)
