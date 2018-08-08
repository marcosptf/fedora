#!/usr/bin/env python2
#encoding: UTF-8
import mock
import os
import os.path
import tempfile

def rm(filename):
    os.remove(filename)


tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

def test_rm():
    with open(tmpfilepath, "w") as f:
        f.write("Delete me!")

    # remove the file
    rm(tmpfilepath)
    # test that it was actually removed
    assert os.path.isfile(tmpfilepath) is False


