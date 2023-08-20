# this challenge has to solved by importing the calendar module

import calendar

month, day, year = map(int, input().split())
weekday = calendar.weekday(year, month, day)
week_day_name = calendar.day_name[weekday].upper()
print(week_day_name)
