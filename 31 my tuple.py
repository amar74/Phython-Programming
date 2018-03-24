Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # tuple function
>>> mytuple=(1,2,'lamb','apple',9)
>>> len(mytuple)
5
>>> mytuple=(78,84,112,-91,43,221)
>>> max(mytuple)
221
>>> min(mytuple)
-91
>>> 
=============================== RESTART: Shell ===============================
>>> #discnory
>>> movies={1994:"Dil hai tumhara",1997:"starwar",2000:"startrek"}
>>> movies
{1994: 'Dil hai tumhara', 1997: 'starwar', 2000: 'startrek'}
>>> len(movies)
3
>>> movies.keys()
dict_keys([1994, 1997, 2000])
>>> movies.values()
dict_values(['Dil hai tumhara', 'starwar', 'startrek'])
>>> new={1972:"Wo Yara rab ruth jane de" 1995:"My birthday"}
SyntaxError: invalid syntax
>>> new={1992:"wo yara rab ruth jane de", 1995:"my birth day"}
>>> new
{1992: 'wo yara rab ruth jane de', 1995: 'my birth day'}
>>> movies.update(new)
>>> movies
{1994: 'Dil hai tumhara', 1997: 'starwar', 2000: 'startrek', 1992: 'wo yara rab ruth jane de', 1995: 'my birth day'}
>>> movies.clear()
>>> movies
{}
>>> 
=============================== RESTART: Shell ===============================
>>> 
