# 4-та задача
import datetime
import calendar

current_date = datetime.datetime.now()
print(current_date)

current_year = datetime.datetime.now().year
print(current_year)

current_week = datetime.datetime.now().weekday()
print(current_week)

current_day_of_the_week = datetime.datetime.now()
print(calendar.day_name[current_day_of_the_week.weekday()])

day_of_year = datetime.date.today().strftime("%j")
print(day_of_year)

day_of_month = datetime.date.today().strftime("%d")
print(day_of_month)

day_of_week = datetime.date.today().strftime("%w")
print(day_of_week)