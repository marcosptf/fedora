#!/usr/bin/env python2
#encoding: UTF-8

import os
import os.path
import mock
import unittest


class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rm(filename):
        if os.path.isfile(filename):
            os.remove(filename)


class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('mock_lab_5.os.path')
    @mock.patch('mock_lab_5.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()

        # set up the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        
        # make the file 'exist'
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")



