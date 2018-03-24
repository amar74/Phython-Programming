Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str1="Hey!!..  Amar"
>>> str1.capitalize()
'Hey!!..  amar'
>>> str1
'Hey!!..  Amar'
>>> str1="""Amar is good student
Amar is upset
he working on webgax-quassarian innovation pvt. ltd
lovinng with own work"""
>>> str1
'Amar is good student\nAmar is upset\nhe working on webgax-quassarian innovation pvt. ltd\nlovinng with own work'
>>> str1.count('Amar')
2
>>> str1="iloveyou.com"
>>> str1.endwith('.org')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    str1.endwith('.org')
AttributeError: 'str' object has no attribute 'endwith'
>>> str1.endswith('.org')
False
>>> str1.endswith('.com')
True
>>> str1="catch me if you can"
>>> str1.find('you')
12
>>> str1.find('amar')
-1
>>> str1.find('me')
6
>>> str1="hello Amar"
>>> str1.islower
<built-in method islower of str object at 0x0000021A0C8FACB0>
>>> str1.islower()
False
>>> str1.isuuper()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    str1.isuuper()
AttributeError: 'str' object has no attribute 'isuuper'
>>> str1="HAVE A NICE DAY"
>>> str1.isupper()
True
>>> len(str1)
15
>>> str1="ee fwlvh fe bedbwfuog fycgnwieucfh8cwgrnfiouwhouegfcw8oegfpxiasodiubcwyfoenrfynheijhf9yeyggnfpehhb08bvy[ewr87vb9fnwewfgvpemfcjshnaiufcynwiefhcwcfcpwhfpinwgfoygwnufhwpqhowqygeiiwemhfocge"
>>> len(str1)
185
>>> str1.lower()
'ee fwlvh fe bedbwfuog fycgnwieucfh8cwgrnfiouwhouegfcw8oegfpxiasodiubcwyfoenrfynheijhf9yeyggnfpehhb08bvy[ewr87vb9fnwewfgvpemfcjshnaiufcynwiefhcwcfcpwhfpinwgfoygwnufhwpqhowqygeiiwemhfocge'
>>> str2="DBSOUEYFOYEGONEFV 8YEGFVNYEGFNYNGWNEGFOUGUBREGBYER8FE8R"
>>> len(str2)
55
>>> str2.lower()
'dbsoueyfoyegonefv 8yegfvnyegfnyngwnegfougubregbyer8fe8r'
>>> str1="!!!!!!!!!!!!!!!! wht is your name?"
>>> str1.lstrip('!')
' wht is your name?'
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> str1="I have lp"
>>> str1
'I have lp'
>>> str1.replace('lp', 'laptop')
'I have laptop'
>>> str1="Amarnath Rana"
>>> str1.split()
['Amarnath', 'Rana']
>>> str1="#########Good Morning##############"
>>> str1.strip('#')
'Good Morning'
>>> str1="#########@@@@@@@@@@@@@@good morning@##########$$$$$$$$"
>>> str1.strip('#','@')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    str1.strip('#','@')
TypeError: strip() takes at most 1 argument (2 given)
>>> str1.strip('#')
'@@@@@@@@@@@@@@good morning@##########$$$$$$$$'
>>> str1.strip('@')
'#########@@@@@@@@@@@@@@good morning@##########$$$$$$$$'
>>> str1="I LOVE you my Love"
>>> str1.swapcase()
'i love YOU MY lOVE'
>>> str1.title()
'I Love You My Love'
>>> 
=============================== RESTART: Shell ===============================
>>> mylist=[1,2,3,4,5,6,7,8,9,0]
>>> len(mylist)
10
>>> max(mylist)
9
>>> min(mylist)
0
>>> count(mylist)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    count(mylist)
NameError: name 'count' is not defined
>>> mylist1[1,2,3,4,1,2,5,1,5,4,3,2,3,6,5,2,6,,1,2,3,3,1,1,2,]
SyntaxError: invalid syntax
>>> mylist1[1,2,3,1,2,3,3,5,6,7,8,9,5,2,1,3,3,6,2,3,2,3,2,1,3,6,8,9,3,2,1,]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    mylist1[1,2,3,1,2,3,3,5,6,7,8,9,5,2,1,3,3,6,2,3,2,3,2,1,3,6,8,9,3,2,1,]
NameError: name 'mylist1' is not defined
>>> mylist1=[1,2,3,1,2,3,5,6,5,9,6,9,8,7,5,2,2,3,2,1,2,3,6,2,1,2,3,5,1,2,3,5,4,2,3,2,1,5,2,3,2,1,2,3,6,1,2,3,2]
>>> mylist1.count(1)
8
>>> mylist1.count(2)
16
>>> mylist1.count(3)
10
>>> mylist1.append(8)
>>> mylist1
[1, 2, 3, 1, 2, 3, 5, 6, 5, 9, 6, 9, 8, 7, 5, 2, 2, 3, 2, 1, 2, 3, 6, 2, 1, 2, 3, 5, 1, 2, 3, 5, 4, 2, 3, 2, 1, 5, 2, 3, 2, 1, 2, 3, 6, 1, 2, 3, 2, 8]
>>> mylist.append(78)
>>> mylist
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 78]
>>> 
=============================== RESTART: Shell ===============================
>>> mylist=[4,1,9,7,4,3,5,2,5,6,7]
>>> mylist.insert(5,89)
>>> mylist
[4, 1, 9, 7, 4, 89, 3, 5, 2, 5, 6, 7]
>>>  mylist.remove(9)
 
SyntaxError: unexpected indent
>>> mylist.remove(9)
>>> mylist
[4, 1, 7, 4, 89, 3, 5, 2, 5, 6, 7]
>>> mylist.reverse()
>>> mylist
[7, 6, 5, 2, 5, 3, 89, 4, 7, 1, 4]
>>> mylist.sort()
>>> mylist
[1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 89]
>>> 
