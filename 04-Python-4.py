workhours = float(input('Enter hours worked: '))

hourly_rate = float(input('\nEnter hourly rate: '))

hourly_pay = 40 * hourly_rate

if workhours > 40:
        overtime = (workhours - 40) * (1.5 * hourly_rate)

pay = hourly_pay + overtime

print(round(pay))