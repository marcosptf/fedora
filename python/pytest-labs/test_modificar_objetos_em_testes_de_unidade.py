
from unittest.mock import patch
import example

@patch(example.func)
def test1(x, mock_func):
    
    #exemplo usando o patch como decorator
    #usa example.func modificada
    example.func(x)
    mock_func.assert_called_with(x)
    
    #exemplo usando o patch como objeto de contexto
    with patch('example.func') as mocker:
        #usa example.func modificada
        example.func(x)
        mocker.assert_called_with(x)


    #exemplo usanod o patch para modificar os objetos manualmente
    @patch('example.func1')
    @patch('example.func2')
    @patch('example.func3')
    def test1(mock_func3, mock_func2, mock_func1):
        pass
    
    #exemplo usando patch como objeto de contexto dentro de uma function
    def test2():
        with patch('example.patch1') as mock1, \
             patch('example.patch2') as mock2, \
             patch('example.patch3') as mock3:
            pass
        

