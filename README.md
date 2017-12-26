Python Umm Al-Qura Calender
===========================

Python Umalqurra Calender is an API that will give you the ability to convert Gregorian to Hijri and hijri to Gregorian
it will give you the day name in arabic and english , and the month name in Hijri arabic and Gregorian.

Thanks for Khalid Al-hussayen : https://pypi.python.org/pypi/umalqurra/0.2 

Install
-------
	sudo pip3 install ummalqura

	or

	sudo pip3 install git+https://github.com/borni-dhifi/ummalqura.git

Features: 
---------

-  Convert Gregorian to Hijri

-  Convert Hijri to Gregorian

-  give the arabic name of the hijri month

-  give the english name of the gregorian month

-  give the day name in Arabic and English

-  give the current day both in Hijri and Gregorian


Usage
-----
 
	#!/usr/bin/env python3

	from ummalqura.hijri_date import HijriDate
	from datetime import date

	# create the object with Gregorian date
	um = HijriDate(2017, 12, 26, gr=True)

	# hijri month
	print('hijri month: ', um.month)  # 4
	# Hijri year
	print('hijri year: ', um.year)  # 1439
	# arabic day name
	print('arabic day name: ', um.day_name)  # الثلاثاء
	# english day name
	print('english day name: ', um.day_name_en)  # Tuesday
	# arabic hijri month name
	print('arabic hijri month name: ', um.month_name)  # ربيع الثاني
	# english gregorian month name
	print('english gregorian month name: ', um.month_name_gr)  # December
	# gregorian year
	print('gregorian year: ', um.year_gr)  # 2017
	# gregorian month
	print('gregorian month: ', um.month_gr)  # 12
	# gregorian day
	print('gregorian day: ', um.day_gr)  # 26

	# current hijri month
	print('current_month: ', HijriDate.current_month())  # 4
	# the gregorian date corresponding to the first day of the given hijri month/year
	print('first day: ', HijriDate.month_start_date(4))  # 2017-12-19
	print('first day: ', HijriDate.month_start_date(4, 1439))  # 2017-12-19
	# the gregorian date corresponding to the last day of the given hijri month/year
	print('last day: ', HijriDate.month_end_date(4))   # 2018-01-17
	print('last day: ', HijriDate.month_end_date(4, 1439))   # 2018-01-17
	# the hijri month for the given gregorian date
	print('hijri month: ', HijriDate.hijri_month_from_date(date.today()))  # 4
	# the hijri year for the given gregorian date
	print('hijri year: ', HijriDate.hijri_year_from_date(date.today()))  # 1439
	# convert the given gregorian date to hijri date
	print('hijri date: ', HijriDate.get_hijri_date(date.today()))  # 1439-04-08
	# convert the given hijri date to gregorian date
	print('georing date: ', HijriDate.get_georing_date('1439-04-08'))  # 2017-12-26


