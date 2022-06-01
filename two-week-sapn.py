import datetime
#05/11/22 - 05/25/22
u = datetime.datetime.strptime("03/16/2022","%m/%d/%Y")
for i in range(100):
    d = datetime.timedelta(days=14)
    a = u.strftime("%m/%d/%Y")   
    a1 = a[:-4] + a[-2:]
    u = u + d
    u1 = u.strftime("%m/%d/%Y")
    u1 = u1[:-4] + u1[-2:]
    print(a1 + ' - ' +  u1)
