# -*- coding: utf-8 -*-
"""
    Flaskr Tests
    ~~~~~~~~~~~~
    Tests the Flaskr application.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
    
  / Flaskr /

                 a minimal blog application


    ~ What is Flaskr?

      A sqlite powered thumble blog application

    ~ How do I use it?

      1. edit the configuration in the factory.py file or
         export a FLASKR_SETTINGS environment variable
         pointing to a configuration file or pass in a
         dictionary with config values using the create_app
         function.

      2. install the app from the root of the project directory

         pip install --editable .

      3. instruct flask to use the right application

         export FLASK_APP=flaskr.factory:create_app()

      4. initialize the database with this command:

         flask initdb

      5. now you can run flaskr:

         flask run

         the application will greet you on
         http://localhost:5000/

    ~ Is it tested?

      You betcha.  Run `python setup.py test` to see
      the tests pass.
    
"""

from setuptools import setup, find_packages

setup(
    name='flaskr',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
