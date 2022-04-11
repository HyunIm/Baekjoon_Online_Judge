now = list(map(int, input().split(':')))
start = list(map(int, input().split(':')))

now_time = now[0]*3600 + now[1]*60 + now[2]
start_time = start[0]*3600 + start[1]*60 + start[2]
gap_time = start_time - now_time
if gap_time < 0:
    gap_time += 60*60*24
gap_hour, gap_minute, gap_second = gap_time//3600, gap_time%3600//60, gap_time%60

print(str(gap_hour).zfill(2), str(gap_minute).zfill(2), str(gap_second).zfill(2), sep=':')
