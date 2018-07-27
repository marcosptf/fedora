#number formating
#http://babel.pocoo.org/en/latest/numbers.html

from babel.numbers import format_number, format_decimal, format_percent
>>> format_decimal(1.2345, locale='en_US')
u'1.234'
>>> format_decimal(1.2345, locale='sv_SE')
u'1,234'
>>> format_decimal(12345, locale='de_DE')
u'12.345'


#Pattern Syntax
>>> format_decimal(-1.2345, format='#,##0.##;-#', locale='en')
u'-1.23'
>>> format_decimal(-1.2345, format='#,##0.##;(#)', locale='en')
u'(1.23)'


#Rounding Modes
>>> from babel.numbers import decimal, format_decimal
>>> with decimal.localcontext(decimal.Context(rounding=decimal.ROUND_DOWN)):
>>>    txt = format_decimal(123.99, format='#', locale='en_US')
>>> txt
u'123'

>>> from decimal import localcontext, Context, ROUND_DOWN
>>> from babel.numbers import format_decimal
>>> with localcontext(Context(rounding=ROUND_DOWN)):
>>>    txt = format_decimal(123.99, format='#', locale='en_US')
>>> txt
u'124'


#Parsing Numbers
>>> from babel.numbers import parse_decimal, parse_number
>>> parse_decimal('1,099.98', locale='en_US')
1099.98
>>> parse_decimal('1.099,98', locale='de')
1099.98
>>> parse_decimal('2,109,998', locale='de')
Traceback (most recent call last):
NumberFormatError: '2,109,998' is not a valid decimal number

