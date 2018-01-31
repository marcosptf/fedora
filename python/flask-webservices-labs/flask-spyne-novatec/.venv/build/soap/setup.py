# encoding: utf-8
from __future__ import absolute_import, print_function
# import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version__ = '0.0.1pre'
__author__ = 'Dmitry Orlov <me@mosquito.su>'


supports = {
    'install_requires': [
        'lxml',
        'requests',
    ]
}

# if sys.version_info >= (3,):
#     supports['install_requires'].append()
# else:
#     supports['install_requires'].append()

setup(
    name='soap',
    version=__version__,
    author=__author__,
    author_email='me@mosquito.su',
    license="LGPLv3",
    description="Modern SOAP library.",
    platforms="all",
    url="http://github.com/mosquito/soap",
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
    ],
    long_description=open('README.rst').read(),
    packages=['soap.client', 'soap.server', 'soap.common'],
    **supports
)