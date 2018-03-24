Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: C:/Users/Amarnath Rana/Desktop/python/time python.py =======
Hello Amarnath
>>> 
======= RESTART: C:/Users/Amarnath Rana/Desktop/python/time python.py =======
Hello Amarnath
Traceback (most recent call last):
  File "C:/Users/Amarnath Rana/Desktop/python/time python.py", line 4, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
>>> import calender
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
>>> 
=============================== RESTART: Shell ===============================
>>> import calendar
>>> print(calendar.month(1995,10))
    October 1995
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

>>> print(calendar.calendar(2018,2,1,15))
                                           2018

      January                            February                            March
Mo Tu We Th Fr Sa Su               Mo Tu We Th Fr Sa Su               Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                         1  2  3  4                         1  2  3  4
 8  9 10 11 12 13 14                5  6  7  8  9 10 11                5  6  7  8  9 10 11
15 16 17 18 19 20 21               12 13 14 15 16 17 18               12 13 14 15 16 17 18
22 23 24 25 26 27 28               19 20 21 22 23 24 25               19 20 21 22 23 24 25
29 30 31                           26 27 28                           26 27 28 29 30 31

       April                               May                                June
Mo Tu We Th Fr Sa Su               Mo Tu We Th Fr Sa Su               Mo Tu We Th Fr Sa Su
                   1                   1  2  3  4  5  6                            1  2  3
 2  3  4  5  6  7  8                7  8  9 10 11 12 13                4  5  6  7  8  9 10
 9 10 11 12 13 14 15               14 15 16 17 18 19 20               11 12 13 14 15 16 17
16 17 18 19 20 21 22               21 22 23 24 25 26 27               18 19 20 21 22 23 24
23 24 25 26 27 28 29               28 29 30 31                        25 26 27 28 29 30
30

        July                              August                           September
Mo Tu We Th Fr Sa Su               Mo Tu We Th Fr Sa Su               Mo Tu We Th Fr Sa Su
                   1                      1  2  3  4  5                               1  2
 2  3  4  5  6  7  8                6  7  8  9 10 11 12                3  4  5  6  7  8  9
 9 10 11 12 13 14 15               13 14 15 16 17 18 19               10 11 12 13 14 15 16
16 17 18 19 20 21 22               20 21 22 23 24 25 26               17 18 19 20 21 22 23
23 24 25 26 27 28 29               27 28 29 30 31                     24 25 26 27 28 29 30
30 31

      October                            November                           December
Mo Tu We Th Fr Sa Su               Mo Tu We Th Fr Sa Su               Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                         1  2  3  4                               1  2
 8  9 10 11 12 13 14                5  6  7  8  9 10 11                3  4  5  6  7  8  9
15 16 17 18 19 20 21               12 13 14 15 16 17 18               10 11 12 13 14 15 16
22 23 24 25 26 27 28               19 20 21 22 23 24 25               17 18 19 20 21 22 23
29 30 31                           26 27 28 29 30                     24 25 26 27 28 29 30
                                                                      31

>>> calendar.isleap(2008)
True
>>> calendar.isleap(2018)
False
>>> 
