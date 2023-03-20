# DATETIME MODULE IN PYTHON
# to get current date and time
import datetime
now= datetime.datetime.now()
print(now)

# to get current date
date_today= datetime.date.today()
print(date_today)

# by importing only date class
from datetime import date
d= date(2023, 3, 15 )
print(d)

# current date using today
today_date = date.today()
print("today's date is: ", today_date)

# getting date from a timestamp
timestamp= date.fromtimestamp(1365468997)
print("date", timestamp)

# for printing today's year, month and day
today= date.today()
print("current year is", today.year)
print("current month is", today.month)
print("current day is", today.day)

# Timedelta- a timedelta object represents the difference between two dates or times.
t1= date(year=2010, month=10, day=31)
t2= date(year=2003, month=4, day=29)
t=t1-t2
print("difference is", t)

# strftime() method in python
from datetime import datetime
now= datetime.now()
t= now.strftime("%H:%M:%S")
print("time is", t)

d1= now.strftime("%m/%d/%Y, %H:%M:%S")
print("date:", d1)   # mm/dd/yy H:M:S format

d2= now.strftime("%d/%m/%Y, %H:%M:%S")
print("date is", d2)  # dd/mm/yy H:M:S format

# stprtime() method in python
from datetime import datetime
date_str = "15 MARCH, 2023"
print("date is", date_str)
