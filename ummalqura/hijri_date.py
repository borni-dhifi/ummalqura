# -*- coding: utf-8 -*-
'''
This is an API for Hijri Umalqurra Calendar,
it was developed  by khalid Al-hussayen 1436-3-15 2015-1-6.
The algrothem of converting hijri to  Gregorian is in hijri.py
This Api will give the ability to convert Gregorian To Hijri or Hijri to Gregorian with the day and month names in Hijri and Gregorian
You can query for the current day in both Hijri and Gregorian
'''
__author__ = 'Khalid & Borni'
from ummalqura.hijri import Umalqurra
from datetime import date, datetime

DAYS = {1: 30,
        2: 29,
        3: 30,
        4: 30,
        5: 30,
        6: 29,
        7: 29,
        8: 30,
        9: 29,
        10: 29,
        11: 30,
        12: 29}

class HijriDate:
    #day in hijri
    day = -1
    #month in hijri
    month = -1
    #month len
    month_len = -1
    #year in hijri
    year = -1
    day_gr = -1
    month_gr = -1
    year_gr = -1
    #day bane in arabic
    day_name = ''
    #month name in hijri
    month_name = ''
    month_dict = {1:'محرم', 2:'صفر', 3:'ربيع الأول', 4:'ربيع الثاني', 5:'جمادي الأولى', 6:'جمادي الآخرة',
                  7:'رجب', 8:'شعبان', 9:'رمضان', 10:'شوال', 11:'ذو القعدة', 12:'ذو الحجة'}

    day_dict = {'Saturday':'السبت','Sunday':'الاحد','Monday':'الاثنين','Tuesday':'الثلاثاء',
                'Wednesday':'الاربعاء','Thursday':'الخميس','Friday':'الجمعة',
                'samedi':'السبت','dimanche':'الاحد','lundi':'الاثنين','mardi':'الثلاثاء',
                'mercredi':'الاربعاء','jeudi':'الخميس','vendredi':'الجمعة'}

    month_name_gr = ''
    day_name_en = ''
    def __init__(self,year=None,month=None,day=None,gr=False):
        if year != None and month != None and day != None:
            if gr == False:
                self.set_date(year,month,day)
            else:
                self.set_date_from_gr(year,month,day)
    #Set dates if the date send by user is Gregorian
    def set_date_from_gr(self,year,month,day):
        um = Umalqurra()
        self.day_gr, self.month_gr, self.year_gr = day, month, year
        self.year, self.month, self.day, self.month_len = um.gegorean_to_hijri(year,month,day)
        self.month_name = self.month_dict[self.month]
        date_gr = date(year,month,day)
        self.day_name_en = date_gr.strftime("%A")
        self.day_name = self.day_dict[self.day_name_en]
        self.month_name_gr = date_gr.strftime("%B")
    #Set dates if date send by user is Hijri
    def set_date(self,year,month,day):
        um = Umalqurra()
        self.day, self.month, self.year = day, month, year
        self.month_name = self.month_dict[month]
        self.year_gr, self.month_gr, self.day_gr = um.hijri_to_gregorian(year,month,day)
        date_gr = date(int(self.year_gr),int(self.month_gr),int(self.day_gr))
        self.day_name_en = date_gr.strftime("%A")
        self.day_name = self.day_dict[self.day_name_en]
        self.month_name_gr = date_gr.strftime("%B")

    @classmethod
    def today(cls):
        today = date.today()
        hijri_date = HijriDate(today.year,today.month,today.day,True)
        return hijri_date

    @classmethod
    def current_month(self):
        """Get the current hijri month.
        :return: <int> month number : 1..12
        """
        um = self.today()
        return um.month

    @classmethod
    def month_start_date(self, month, year=False):
        """Get the gregorian date corresponding to the first day of the given hijri month/year.
        :param month: int hijri month
        :param year: int hijri year
        :return: date
        """
        if not year:
            year = self.today().year
        um = HijriDate(year, month, 1)
        start_date = Umalqurra().hijri_to_gregorian(um.year, um.month, um.day)
        return date(start_date[0], start_date[1], start_date[2])

    @classmethod
    def month_end_date(self, month, year=False):
        """Get the gregorian date corresponding to the last day of the given hijri month/year.
        :param month: int hijri month
        :param year: int hijri year
        :return: date
        """
        if not year:
            year = self.today().year
        um = HijriDate(year, month, DAYS[month])
        start_date = Umalqurra().hijri_to_gregorian(um.year, um.month, um.day)
        return date(start_date[0], start_date[1], start_date[2])

    @classmethod
    def hijri_month_from_date(self, date):
        """Get the hijri month for the given gregorian date.
        :param date: gregorian date
        :return: <int> month
        """
        hijri_date = HijriDate(date.year, date.month, date.day, gr=True)
        return hijri_date.month

    @classmethod
    def hijri_year_from_date(self, date):
        """Get the hijri year for the given gregorian date.
        :param date: gregorian date
        :return: <int> year
        """
        hijri_date = HijriDate(date.year, date.month, date.day, gr=True)
        return hijri_date.year

    @classmethod
    def get_hijri_date(self, date_str, separator='-'):
        """Convert georging date to hijri date.
        :param date: <str> gregorian date
        :return hijri date as a string value
        """
        date_str = datetime.strptime(str(date_str), '%Y-%m-%d').date()
        hijri_date = HijriDate(date_str.year, date_str.month, date_str.day, gr=True)
        return str(hijri_date.year).zfill(4) + separator + str(hijri_date.month).zfill(2) + separator + str(hijri_date.day).zfill(2)

    @classmethod
    def get_georing_date(self,str_hijri_date):
        """Convert hijri date to georing date.
        :param date: hijri date YYYY-MM-DD
        :return georing date as a string value
        """
        year = int(str_hijri_date[:4])
        month = int(str_hijri_date[5:7])
        day = int(str_hijri_date[8:10])
        res_date = Umalqurra().hijri_to_gregorian(year, month, day)
        return date(res_date[0], res_date[1], res_date[2])


