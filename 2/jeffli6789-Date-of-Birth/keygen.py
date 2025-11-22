from datetime import date, timedelta
import random

keys = []

i = 0
today = date.today()
while(True):
    year = 128 + i*256
    if(year >= date.today().year):
        break
    keys.append(date(year = today.year - year, month = today.month, day =
        today.day) + timedelta(days = 1))
    i += 1

key = keys[random.randint(0, len(keys)-1)]
print("{}/{}/{}".format(key.month, key.day, key.year))
