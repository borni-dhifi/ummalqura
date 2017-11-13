#!/usr/bin/env python3

from ummalqura.hijri_date import HijriDate
#create the object with Gregorian date
um = HijriDate(1989,1,10,gr=True)
#to see the day in Hijri
um.day # result : 3.0
#to see the month in Hijri
um.month #result is 6.0
#year
um.year #1409
#day name in arabic
print (um.day_name) #الثلاثاء
#day in english
um.day_name_en #Tuesday
#month in Hijri Arabic
print (um.month_name) #جمادي الاخرة
#month in Gregorian English
um.month_name_gr #January
#year in Gregorian
um.year_gr #1989
#month in Gregorian
um.month_gr # 1
#day in Gregorian
um.day_gr # 10
