Python Umm Al-Qura Calender
===========================

Python Umalqurra Calender is an API that will give you the ability to convert Gregorian to Hijri and hijri to Gregorian
it will give you the day name in arabic and english , and the month name in Hijri arabic and Gregorian.

Thanks for Khalid Al-hussayen : https://pypi.python.org/pypi/umalqurra/0.2 


Features: 
---------

-  Convert Gregorian to Hijri

-  Convert Hijri to Gregorian

-  give the arabic name of the hijri month

-  give the english name of the gregorian month

-  give the day name in Arabic and English

-  give the current day both in Hijri and Gregorian


Install:
-------

sudo pip3 install git+https://github.com/borni-dhifi/ummalqura.git



Usage
-----
 
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

