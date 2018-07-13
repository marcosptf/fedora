#!/usr/bin/env python2
#encoding: UTF-8
import mock

class Target(object):
    def apply(value):
        return value

def method(target, value):
    return target.apply(value)

#pytest using mock.Mock() instance
def test_method():
    target = mock.Mock()
    method(target, "value")
    target.apply.assert_called_with("value")


