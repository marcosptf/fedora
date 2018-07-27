#class locale
>>> from babel import Locale
>>> locale = Locale('en', 'US')
>>> locale.territories['US']
u'United States'
>>> locale = Locale('es', 'MX')
>>> locale.territories['US']
u'Estados Unidos'


#Likely Subtags
>>> from babel import Locale
>>> Locale.parse('zh_TW')
Locale('zh', territory='TW', script='Hant')

>>> Locale.parse('und_AZ')
Locale('az', territory='AZ', script='Latn')
>>> Locale.parse('und_DE')
Locale('de', territory='DE')

#Locale Display Names
>>> l = Locale.parse('de_DE')
>>> l.get_display_name('en_US')
u'German (Germany)'
>>> l.get_display_name('fr_FR')
u'allemand (Allemagne)'
>>> l.get_language_name('de_DE')
u'Deutsch'
>>> l.get_language_name('it_IT')
u'tedesco'
>>> l.get_territory_name('it_IT')
u'Germania'
>>> l.get_territory_name('pt_PT')
u'Alemanha'


#Calendar Display Names
>>> locale = Locale('es')
>>> month_names = locale.months['format']['wide'].items()
>>> for idx, name in sorted(month_names):
...     print name
enero
febrero
marzo
abril
mayo
junio
julio
agosto
septiembre
octubre
noviembre
diciembre




