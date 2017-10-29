"""
estudos de funcoes pythons 
"""

[root@localhost ~]# python
Python 2.7.10 (default, Aug 21 2015, 23:37:50) 
[GCC 4.8.3 20140911 (Red Hat 4.8.3-7)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> lambda x: x + 2(2)        
<function <lambda> at 0xb766c614>
>>> a = lambda x: x + 2(2)
>>> a
<function <lambda> at 0xb766c80c>
>>> dir(a)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> a.__call__
<method-wrapper '__call__' of function object at 0xb766c80c>
>>> print(a)
<function <lambda> at 0xb766c80c>
>>> b = lambda x: x + 2
>>> print(b)   
<function <lambda> at 0xb766c614>
>>> print(b(4))
6
>>> 
