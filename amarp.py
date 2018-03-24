Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\Amarnath Rana\Desktop\hello.py ==============
hello amar
>>> 
=============================== RESTART: Shell ===============================
>>> var1=100
>>> var1
100
>>> var1=var2=var3=100
>>> var1
100
>>> var2
100
>>> var3
100
>>> var1,var2,var3=150,200,300 "string"
SyntaxError: invalid syntax
>>> var1,var2,var3=150,200,300, "string"
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    var1,var2,var3=150,200,300, "string"
ValueError: too many values to unpack (expected 3)
>>> var1,var2,var3=150,200,300
>>> var1
150
>>> var2
200
>>> var3
300
>>> var1,var2,var3=150,200,"string"
>>> var1
150
>>> var3
'string'
>>> var2
200
>>> 
=============================== RESTART: Shell ===============================
>>>  a=5
 
SyntaxError: unexpected indent
>>> a
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> var1=100
>>> var1
100
>>> a=5
>>> a
5
>>> 
>>> a=7
>>> a
7
>>> b=8
>>> b
8
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> myvar=7-4k
SyntaxError: invalid syntax
>>> mayvar=7-4j
>>> myvar
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    myvar
NameError: name 'myvar' is not defined
>>> myvar=7-4j
>>> myvar
(7-4j)
>>> yourvar=3+4j
>>> yourvar
(3+4j)
>>> myvar+yourvar
(10+0j)
>>> myvar-yourvar
(4-8j)
>>> myvar*yourvar
(37+16j)
>>> myvar/yourvar
(0.2-1.6j)
>>> 
=============================== RESTART: Shell ===============================
>>> str='Hello Amarnath'
>>> str
'Hello Amarnath'
>>> str[0]
'H'
>>> str[0:4]
'Hell'
>>> str[4]
'o'
>>> str[0:5]
'Hello'
>>> str[5:]
' Amarnath'
>>> str*5
'Hello AmarnathHello AmarnathHello AmarnathHello AmarnathHello Amarnath'
>>> str+
SyntaxError: invalid syntax
>>> str+8
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    str+8
TypeError: must be str, not int
>>> str/5
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    str/5
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> str+"Hey whats going on?"
'Hello AmarnathHey whats going on?'
>>> 
=============================== RESTART: Shell ===============================
>>> mylist=['one','two','3','four','5','6.075','6+5j']



