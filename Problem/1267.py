def YPlan(time):
    return (time//30+1) * 10

def MPlan(time):
    return (time//60+1) * 15

N = int(input())
callTimes = list(map(int, input().split()))

YPlanRate = 0
MPlanRate = 0

for time in callTimes:
    YPlanRate += YPlan(time)
    MPlanRate += MPlan(time)

if YPlanRate < MPlanRate:
    print('Y', YPlanRate)
elif YPlanRate > MPlanRate:
    print('M', MPlanRate)
elif YPlanRate == MPlanRate:
    print('Y M', YPlanRate)
