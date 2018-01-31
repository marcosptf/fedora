# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from setuptools import setup, find_packages

version = "1.2"

setup(
      name = "sec-wall",
      version = version,

      scripts = ["scripts/sec-wall"],

      author = "Dariusz Suchojad",
      author_email = "dsuch at gefira.pl",
      url = "http://sec-wall.gefira.pl/",
      description = "A feature packed security proxy",
      long_description = "sec-wall is a feature packed security proxy supporting SSL/TLS, WS-Security, HTTP Auth Basic/Digest, extensible authentication schemes based on custom HTTP headers and XPath expressions, powerful URL matching/rewriting and an optional headers enrichment. It's a security wall you can conveniently fence the otherwise defenseless backend servers with.",
      platforms = ["OS Independent"],
      license = "GNU Lesser General Public License v3 (LGPLv3)",

      package_dir = {"":b"src"},
      packages = find_packages(b"src"),

      namespace_packages = [b"secwall"],

      zip_safe = False,

      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Firewalls'
        ],
)
