[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import py.test
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'py'
>>> java = "javascripter"
>>> java[0]
'j'
>>> java[5]
'c'
>>> java[0:4]
'java'
>>> pyhton_list = [0,1,2,3,4,5]
>>> python_list = [0,1,2,3,4,5]
>>> python_list
[0, 1, 2, 3, 4, 5]
>>> len(python_list)
6
>>> a,b,c,d,e = 0,1,2,3,4
>>> a
0
>>> b
1
>>> c
2
>>> d
3
>>> e
4
>>> f
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'f' is not defined
>>> python_list.reverse()
>>> python_list
[5, 4, 3, 2, 1, 0]
>>> 
>>> def index():
...     def a():
...         print("def a")
...     def b():
...         print("def b")
...     def c():
...         print("def c")
...     def d():
...         print("def d")
... 
>>> index()
>>> print(index())
None
>>> ;5~
  File "<stdin>", line 1
    ;5~
    ^
SyntaxError: invalid syntax
>>> 
>>> def index():
...     def a():
...         print("def a")
...     a()
... 
>>> index()
def a
>>> 
>>> 
>>> def index():
...     def a():
...         def aa():
...             print("aa")
...         print
... 
>>> 
>>> 
>>> def index():
...     print("index")
...     def a():
...         print("a")
...         def aa():
...             print("aaa")
... 
>>> index()
index
>>> index.a()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'a'
>>> index
<function index at 0x7fa559d918c8>
>>> index.__call__(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: index() takes 0 positional arguments but 1 was given
>>> index.a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'a'
>>> ;5~
  File "<stdin>", line 1
    ;5~
    ^
SyntaxError: invalid syntax
>>> 
>>> 
>>> 

>>> def index():
...     def a():
...         print("a")
...         def aa():
...             print("aa")
...             def aaa():
...                 print("aaa")
...                 def aaaa():
...                     print("aaaa")
...                     def aaaaa():
...                         print("aaaaa")
...                     aaaaa()   
...                 aaaa()
...             aaa()
...         aa()
...     a()
... index()
  File "<stdin>", line 17
    index()
        ^
SyntaxError: invalid syntax
>>> def index():
...     def a():
...         print("a")
...         def aa():
...             print("aa")
...             def aaa():
...                 print("aaa")
Python 3.6.0 (default, Jan 13 2017, 00:00:00) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
