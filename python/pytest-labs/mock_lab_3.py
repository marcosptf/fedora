#!/usr/bin/env python2
#encoding: UTF-8

import os
import mock

def rm(filename):
    os.remove(filename)

@mock.patch('mock_lab_3.os')
def test_rm(mock_os):
    rm("any path")
    # test that rm called os.remove with the right parameters
    mock_os.remove.assert_called_with("any path")

