year='2012'
if (int(year)%4==0 and int(year)%100!=0) or int(year)%400==0:
    print(366)
else:print(365)