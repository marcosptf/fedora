#!/usr/bin/env python2
#encoding: UTF-8

import os
import os.path
import mock

def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)

@mock.patch('mock_lab_4.os')
def test_rm(mock_os):
    rm("any path")
    # test that rm called os.remove with the right parameters
    mock_os.remove.assert_called_with("any path")

@mock.patch('mock_lab_4.os.path')
@mock.patch('mock_lab_4.os')
def test_rm_refactor(mock_os, mock_path):
    # set up the mock
    mock_path.isfile.return_value = False
    rm("any path")
    # test that the remove call was NOT called.
    assert mock_os.remove.called is False

    # make the file 'exist'
    mock_path.isfile.return_value = True
    rm("any path")
    mock_os.remove.assert_called_with("any path")
    assert mock_os.remove.called is True




