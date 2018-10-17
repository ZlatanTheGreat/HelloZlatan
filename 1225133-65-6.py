import datetime
from datetime import timedelta

# 5 задача
five_days_before_today = datetime.date.today() - timedelta(days=5)
print(five_days_before_today)

# 6 задача
yesterday = datetime.date.today() - timedelta(days=1)
today = datetime.date.today()
tommorow = datetime.date.today() + timedelta(days=1)

print(f'\n{yesterday}\n{today}\n{tommorow}')