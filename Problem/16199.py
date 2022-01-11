birthDate = input()
nowDate = input()

birthYear, birthMonth, birthDay = map(int, birthDate.split())
nowYear, nowMonth, nowDay = map(int, nowDate.split())

standardAge = nowYear - birthYear
if birthMonth > nowMonth or (birthMonth==nowMonth and birthDay > nowDay):
    standardAge -= 1

countingAge = nowYear - birthYear + 1
yearAge = nowYear - birthYear

print(standardAge)
print(countingAge)
print(yearAge)
