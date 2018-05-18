"""
Flask-JWT-Simple
-------------------
Flask-JWT-Simple provides barebones jwt endpoint protection for Flask.
"""
from setuptools import setup

setup(name='Flask-JWT-Simple',
      version='0.0.3',
      url='https://github.com/vimalloc/flask-jwt-simple',
      license='MIT',
      author='Landon Gilbert-Bland',
      author_email='landogbland@gmail.com',
      description='Simple JWT integration with Flask',
      long_description='Simple JWT integration with Flask',
      keywords=['flask', 'jwt', 'json web token'],
      packages=['flask_jwt_simple'],
      zip_safe=False,
      platforms='any',
      install_requires=['Flask', 'PyJWT'],
      extras_require={
        'asymmetric_crypto':  ["cryptography"]
      },
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ])
