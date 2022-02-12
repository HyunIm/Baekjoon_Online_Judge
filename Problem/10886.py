N = int(input())
cuteSurvey = [int(input()) for _ in range(N)]

isCute = cuteSurvey.count(1)
isNotCute = cuteSurvey.count(0)

if isCute > isNotCute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
