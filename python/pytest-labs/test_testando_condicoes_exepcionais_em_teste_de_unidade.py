
import unittest

def parse_int(s):
    return int(s)

#cenary-1
class TestConversion(unittest.TestCase):
    
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')

#cenary-2
class TestIO(unittest.TestCase):
    
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
            
        excet IOError as err:
            self.assertRaises(err.errno, errno.ENOENT)
        else:
            self.fail('IOError not raised')
            
        
#cenary-3
class TestConversion(unittest.TestCase):
    
    def test_bad_int(self):
        try:
            r = parse_int('N/A')
        except ValueError as err:
            self.assertEqual(type(err), ValueError)
        else:
            self.fail('ValueError not Raised')

#cenary-4
class TestConversion(unittest.TestCase):
    
    def test_bad_int(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'N/A')
        
#cenary-5
class TestConversion(unittest.TestCase):
    
    def test_bad_int(self):
        with self.assertRaisesRegex(valueError, 'invalid literal .*'):
            r = parse_int('N/A')
            
    
