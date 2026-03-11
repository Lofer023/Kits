from datetime import datetime
import datetime as dt

date = '2024-11-08'
print(date)

date2 = "2024-06-09 14:30:25 INFO: User login successful"
timestamp_str = date2[:19]
print('d',timestamp_str)
format = datetime.strptime(date,"%Y-%m-%d")
format2 = datetime.strptime(timestamp_str,"%Y-%m-%d  %H:%M:%S")

print(format)
print(format2)


import time 

meeting_time = dt.datetime.now()
#time.sleep(1)
print()
print(meeting_time)
end_time = dt.datetime.now()
print(end_time)
print(end_time - meeting_time)


dsp = dt.date(2024,10,8)
print(dsp.year,dsp.month,dsp.day)

login_time = dt.datetime(2024, 4, 9, 18, 30)
print(login_time.date())