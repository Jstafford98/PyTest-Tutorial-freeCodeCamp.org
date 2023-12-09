''' tests the functionality of the shapes.Rectangle class '''

import pytest
from src import shapes

def test_area(my_rectangle : shapes.Rectangle) -> None :
    
    assert my_rectangle.area() == (10 * 20)

def test_perimeter(my_rectangle : shapes.Rectangle) -> None :
    
    assert my_rectangle.perimeter() == ((10*2) + (20*2))
    
def test_not_equal(
    my_rectangle : shapes.Rectangle, 
    weird_rectangle : shapes.Rectangle
) -> None :
    
    assert my_rectangle != weird_rectangle