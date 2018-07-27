#Date and Time
#http://babel.pocoo.org/en/latest/dates.html

>>> from datetime import date, datetime, time
>>> from babel.dates import format_date, format_datetime, format_time

>>> d = date(2007, 4, 1)
>>> format_date(d, locale='en')
u'Apr 1, 2007'
>>> format_date(d, locale='de_DE')
u'01.04.2007'


>>> format_date(d, format='short', locale='en')
u'4/1/07'
>>> format_date(d, format='long', locale='en')
u'April 1, 2007'
>>> format_date(d, format='full', locale='en')
u'Sunday, April 1, 2007'


#Pattern Syntax
>>> d = date(2007, 4, 1)
>>> format_date(d, "EEE, MMM d, ''yy", locale='en')
u"Sun, Apr 1, '07"
>>> format_date(d, "EEEE, d.M.yyyy", locale='de')
u'Sonntag, 1.4.2007'

>>> t = time(15, 30)
>>> format_time(t, "hh 'o''clock' a", locale='en')
u"03 o'clock PM"
>>> format_time(t, 'H:mm a', locale='de')
u'15:30 nachm.'

>>> dt = datetime(2007, 4, 1, 15, 30)
>>> format_datetime(dt, "yyyyy.MMMM.dd GGG hh:mm a", locale='en')
u'02007.April.01 AD 03:30 PM'




#Time Delta Formatting
>>> from datetime import timedelta
>>> from babel.dates import format_timedelta
>>> delta = timedelta(days=6)
>>> format_timedelta(delta, locale='en_US')
u'1 week'

>>> delta = timedelta(days=6)
>>> format_timedelta(delta, threshold=1.2, locale='en_US')
u'6 days'
>>> format_timedelta(delta, granularity='month', locale='en_US')
u'1 month'

>>> from datetime import time
>>> from babel.dates import get_timezone, UTC
>>> dt = datetime(2007, 4, 1, 15, 30, tzinfo=UTC)
>>> eastern = get_timezone('US/Eastern')
>>> format_datetime(dt, 'H:mm Z', tzinfo=eastern, locale='en_US')
u'11:30 -0400'

>>> british = get_timezone('Europe/London')
>>> format_datetime(dt, 'H:mm zzzz', tzinfo=british, locale='en_US')
u'16:30 British Summer Time'

>>> t = get_next_timezone_transition('Europe/Vienna', datetime(2011, 3, 2))
>>> t
<TimezoneTransition CET -> CEST (2011-03-27 01:00:00)>
>>> t.from_offset
3600.0
>>> t.to_offset
7200.0
>>> t.from_tz
'CET'
>>> t.to_tz
'CEST'

>>> from babel.dates import LOCALTZ, get_timezone_name
>>> LOCALTZ
<DstTzInfo 'Europe/Vienna' CET+1:00:00 STD>
>>> get_timezone_name(LOCALTZ)
u'Central European Time'


#Localized Time-zone Names
>>> from babel import Locale
>>> from babel.dates import get_timezone_name, get_timezone
>>> tz = get_timezone('Europe/Berlin')
>>> get_timezone_name(tz, locale=Locale.parse('pt_PT'))
u'Hora da Europa Central'

>>> from datetime import datetime

>>> dt = tz.localize(datetime(2007, 8, 15))
>>> get_timezone_name(dt, locale=Locale.parse('de_DE'))
u'Mitteleurop\xe4ische Sommerzeit'
>>> get_timezone_name(tz, locale=Locale.parse('de_DE'))
u'Mitteleurop\xe4ische Zeit'



