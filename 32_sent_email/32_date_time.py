import datetime as dt
day = dt.datetime.now()
if day.isoweekday() == 1:
   print(f"monday")
   