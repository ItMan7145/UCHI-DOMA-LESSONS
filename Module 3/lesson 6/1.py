import datetime as dt

date = dt.datetime.strptime('27.01.1995', '%d.%m.%Y').date()
date_now = dt.date.today()
Age = date_now - date
print(Age.days // 365)
