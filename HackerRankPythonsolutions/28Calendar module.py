# this challenge has to solved by importing the calendar module

import calendar

month, day, year = map(int, input().split())
weekday = calendar.weekday(year, month, day)
weekdayName = calendar.day_name[weekday].upper()
print(weekdayName)
