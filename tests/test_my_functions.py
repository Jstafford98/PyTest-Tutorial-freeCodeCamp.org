import time
import pytest
from src import my_functions

def test_add() -> None :
    assert my_functions.add(x=1, y=4) == 5
    
def test_add_strings() -> None :
    assert my_functions.add(x='I like ', y='burgers') == 'I like burgers'
    
def test_divide() -> None :
    assert my_functions.divide(x=10, y=5) == 2
    
def test_divide_by_zero() -> None :
    with pytest.raises(ValueError):
        my_functions.divide(x=10, y=0)

@pytest.mark.slow
def test_very_slow() -> None :
    time.sleep(5)
    assert my_functions.divide(x=10, y=5) == 2

    
@pytest.mark.skip(reason='This feature is currently broken.')
def test_add() -> None :
    assert my_functions.add(x=1, y=3) == 3
    
@pytest.mark.xfail(reason='We know we cannot divide by 0')
def test_divide_zero_broken() -> None :
    my_functions.divide(x=4, y=0)