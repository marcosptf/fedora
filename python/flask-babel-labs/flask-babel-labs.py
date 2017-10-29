"""
labs para 
https://pythonhosted.org/Flask-Babel/
"""


from flask import Flask
from flask.ext.babel import Babel
from flask.ext.babel import gettext, ngettext

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
#Babel(app=None, default_locale='en', default_timezone='UTC', date_formats=None, configure_jinja=True)
babel = Babel(app, default_locale='pt_BR', default_timezone='BRST')


gettext(u'A simple string')
gettext(u'Value: %(value)s', value=42)
ngettext(u'%(num)s Apple', u'%(num)s Apples', number_of_apples)