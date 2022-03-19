nowHH, nowMM, nowSS = map(int, input().split(':'))
exeHH, exeMM, exeSS = map(int, input().split(':'))

nowTime = nowHH * 3600 + nowMM * 60 + nowSS
exeTime = exeHH * 3600 + exeMM * 60 + exeSS

waitTime = exeTime-nowTime if exeTime > nowTime else exeTime-nowTime+(24*60*60)
waitHH = waitTime // 60 // 60
waitMM = waitTime // 60 % 60
waitSS = waitTime % 60

print('%02d:%02d:%02d'%(waitHH, waitMM, waitSS))
