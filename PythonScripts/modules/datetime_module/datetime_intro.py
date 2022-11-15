import datetime as dt
import pytz

# r = dt.datetime.today() # only local time
# print(r)
# r = dt.datetime.now() # any timezone
# print(r)

GB = pytz.timezone('GB')
IST = pytz.timezone('Asia/Kolkata')
r = dt.datetime.now(tz=IST)

time = r.strftime('%d-%m-%Y')

# print(r)
# print(time)

res = dt.datetime.fromtimestamp(1668101228)

print(res)