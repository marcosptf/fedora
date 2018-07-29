from io import StringIO
from unittest import TestCase
from unittest.mock import patch

def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)
    
class TestURLPrint(TestCase):

    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'yahoo.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)
        
        with patch('sys.stdout', new=StringIO) as fake_out:
            urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getValue(), expected_url)
