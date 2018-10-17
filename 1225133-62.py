# 2-ра задача
import datetime
from datetime import timedelta

# без функция-----------------------------------
'''year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))

current_date = datetime.date(year,month,day)

next_date = current_date + timedelta(days=1)
print(next_date)'''

date = list(map(int, input().split()))
# без функция-----------------------------------

# със функция-----------------------------------
def nextDate(a):
    next_Date = datetime.date(a[0],a[1],a[2]) + timedelta(days=1)
    print(f'The next date is {next_Date}')

nextDate(date)

# със функция-----------------------------------