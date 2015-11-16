Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=32
>>> print a, hex(a), oct(a), bin(a)
32 0x20 040 0b100000
>>> print 10+10
20
>>> print 10+10.0
20.0
>>> a=12
>>> b=2.0
>>> print a.is_integer(), b.is_integer()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print a.is_integer(), b.is_integer()
AttributeError: 'int' object has no attribute 'is_integer'
>>> a=1.2
>>> print a.is_integer(), b.is_integer()
False True
>>> import math
>>> print round(a), math.ceil(a), math.floor(a)
1.0 2.0 1.0
>>> imprt sys
SyntaxError: invalid syntax
>>> import sya

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    import sya
ImportError: No module named sya
>>> import sys
>>> print sys.getsizeof("a")
22
>>> print sys.getsizeof("ab")
23
>>> a="abcde"
>>> print a[0], a[4]
a e
>>> print a[-1], a[-5]
e a
>>> a="Gachon University"
>>> print a[0:6],"AND"a[-9:]
SyntaxError: invalid syntax
>>> print a[0:6],"AND",a[-9:]
Gachon AND niversity
>>> print [:]
SyntaxError: invalid syntax
>>> print a[:]
Gachon University
>>> print a[::2]
Gco nvriy
>>> 
