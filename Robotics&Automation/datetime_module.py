import datetime
# while True:
#     time_now = datetime.now()
#     current_time = time_now.strftime("%H:%M:%S")
#     current_date = time_now.strftime("%d/%m/%Y")
#     print(f'current time: {current_time}\ncurrent date: {current_date}')
#     command = input("Do you wish to continue?: ")
#     if command == "N" or command == 'n':
#         exit()

tz_obj1 = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
tz_obj2 = datetime.timezone(datetime.timedelta(hours=0, minutes=0))

dt1 = datetime.datetime(day=8, month=2, year=2024, hour=12, minute=35,tzinfo=tz_obj1)
dt2 = datetime.datetime(day=8, month=2, year=2024, hour=8, minute=7,tzinfo=tz_obj2)

print(f'zone1: {dt1}\nzone2: {dt2}')
