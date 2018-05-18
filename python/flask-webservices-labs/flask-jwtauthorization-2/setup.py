"""
Flask-JWTAuthorization
----------------
Adds JWT Authorization framework to your Flask application.

Links
`````

* `Documentation <https://github.com/sergiofcasado/flask-jwtauthorization/wiki>`_
* `Issue Tracker <https://github.com/sergiofcasado/flask-jwtauthorization/issues>`_
* `Source <https://github.com/sergiofcasado/flask-jwtauthorization>`_
"""

from os import path
from codecs import open
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-JWTAuthorization',
    version='0.0.5',
    description='Authorization framework based on JWT for Flask applications',
    long_description=long_description,
    url='https://github.com/sergiofcasado/flask-jwtauthorization',
    author='Sergio Fernandez Casado',
    author_email='sfernand@cern.ch',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='flask jwt json web token authorization',
    packages=['flask_jwtauthorization'],
    install_requires=[
        'Flask>=0.12',
        'PyJWT>=1.4.0'
    ],
)
