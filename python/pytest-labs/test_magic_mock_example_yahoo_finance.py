
import unittest
from unittest.mock import patch
import io
import magic_mock_example_yahoo_finance

sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.95\r
"MSFT",27.72\r
\r
''')

class Tests(unittest.TestCase):
    
    @patch('magic_mock_example_yahoo_finance.urlopen', return_value=sample_data)
    def test_downprices(self, mock_urlopen):
        p = magic_mock_example_yahoo_finance.downprices() 
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {'IBM': 91.1,
                          'AA': 13.25,
                          'MSFT':27.72})
        
        
if __name__ == '__main__':
    unittest.main()



