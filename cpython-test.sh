#!/bin/sh

./python -m test

./python -m test -h

./python -m test -v test_abc

./python -m unittest -v test.test_abc.TestABC

./python -m test -j0

./python -bb -E -Wd -m test -r -w -uall

./python -m test --coverage -D `pwd`/coverage_data

make coverage

make coverage-lcov

make coverage-report
