#!/usr/bin/env python2
#encoding: UTF-8
import mock

class Target(object):
    def apply(value, are_you_sure):
        if are_you_sure:
            return value
        else:
            return None

def method(target, value):
    return target.apply(value)

#pytest using mock.Mock() instance
def test_method():
    target = mock.Mock()
    method(target, "value")
    target.apply.assert_called_with("value")


