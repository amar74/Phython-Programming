Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> address{}
SyntaxError: invalid syntax
>>> address={}
>>> address["Amar"]="amar74.soft@gmail.com"
>>> address["Amarnath"]="amarnathswhh77492@outlook.com"
>>> print (address)
{'Amar': 'amar74.soft@gmail.com', 'Amarnath': 'amarnathswhh77492@outlook.com'}
>>> new={'apple'}
>>> new={'apple':'fruit':'iphone':'phone'}
SyntaxError: invalid syntax
>>> new={'aaple':'fruit', 'iPhone':'phone'}
>>> new
{'aaple': 'fruit', 'iPhone': 'phone'}
>>> print (new)
{'aaple': 'fruit', 'iPhone': 'phone'}
>>> address.keys()
dict_keys(['Amar', 'Amarnath'])
>>> address.values()
dict_values(['amar74.soft@gmail.com', 'amarnathswhh77492@outlook.com'])
>>> 
=============================== RESTART: Shell ===============================
>>> int(55.89)
55
>>> float()36
SyntaxError: invalid syntax
>>> float(36)
36.0
>>> my_string=str(3500)int(55.89)
SyntaxError: invalid syntax
>>> my_string=str(3500)
>>> my_string
'3500'
>>> my_string[1]
'5'
>>> tuple("This is string")
('T', 'h', 'i', 's', ' ', 'i', 's', ' ', 's', 't', 'r', 'i', 'n', 'g')
>>> list("This is Amarnath")
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'A', 'm', 'a', 'r', 'n', 'a', 't', 'h']
>>> chr(65)
'A'
>>> chr(1)
'\x01'
>>> chr(98)
'b'
>>> ord('a')
97
>>> hex(4500)
'0x1194'
>>> oct(4500)
'0o10624'
>>> bin(8)
'0b1000'
>>> bin(15)
'0b1111'
>>> 
=============================== RESTART: Shell ===============================
>>> 10
10
>>> 10+15
25
>>> 52-25
27
>>> 25-65
-40
>>> 50*59
2950
>>> 99*99
9801
>>> 89/98
0.9081632653061225
>>> 5687/48
118.47916666666667
>>> 112+56+98+69+78+-88
325
>>> 59
59
>>> 896+9989+985+-9
11861
>>> 9985+986+985+859-58
12757
>>> 9***8
SyntaxError: invalid syntax
>>> 9**9
387420489
>>> 3***3
SyntaxError: invalid syntax
>>> 3**3
27
>>> 3**2
9
>>> a=5
>>> b=4.8
>>> a==b
False
>>> a!=b
True
>>> a>b
True
>>> b>a
False
>>> b<a
True
>>> c>a
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    c>a
NameError: name 'c' is not defined
>>> b>a
False
>>> a=1
>>> b=1
>>> c=5
>>> b=c
>>> b==c
True
>>> c=a
>>> c==a
True
>>> a=1
>>> b=1
>>> c=5
>>> a==b
True
>>> a==c
False
>>> c==b
False
>>> a==a
True
>>> c>a
True
>>> c<a
False
>>> a<b
False

>>> a>b
False
>>> b<a
False
>>> b>a
False
>>> a=b
>>> 
=============================== RESTART: Shell ===============================
>>> a=25
>>> b=6
>>> bin(a)
'0b11001'
>>> bin(b)
'0b110'
>>> bin(a&b)
'0b0'
>>> bin(a|b)
'0b11111'
>>> 
>>> bin(a^b)
'0b11111'
>>> a=true
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> a=True
>>> b-False
6
>>> a-True
0
>>> a=True
>>> b=False
>>> a and b
False
>>> a or b
True
>>>  not a
 
SyntaxError: unexpected indent
>>> not a
False
>>> not b
True
>>> 
=============================== RESTART: Shell ===============================
>>> str1="I'm Amarnath"
>>> str1
"I'm Amarnath"
>>> "Amarnath" in str1
True
>>> "nath" in str2
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    "nath" in str2
NameError: name 'str2' is not defined
>>> "nath" in str1
True
>>> "afnkj" in str1
False
>>> "'" in str1
True
>>> "m" in str1
True
>>> mylist=[1,2,3,4,5,6,7,8,9,78,96,75,45,788,27,36]
>>> 1 in mylist
True
>>> 3266 in mylist
False
>>> a=78
>>> b=58
>>> b='58'
>>> a is b
False
>>> a=78
>>> b'89'
b'89'
>>> b='89'
>>> a is b
False
>>> a=78
>>> b='78'
>>> a is b
False
>>> 788 in mylist
True
>>> c=78
>>> a is c
True
>>> b is c
False
>>> a is not b
True
>>> b is not a
True
>>> 
=============================== RESTART: Shell ===============================
>>> 5+8*8
69
>>> (5+8)*2
26
>>> 8+9-5*6/2
2.0
>>> (8+9)-(5*6)/2
2.0
>>> (8+(9-5)*6)/2
16.0
>>> 8+(9-5)*6/2
20.0
>>> 
=============================== RESTART: Shell ===============================
>>> 
