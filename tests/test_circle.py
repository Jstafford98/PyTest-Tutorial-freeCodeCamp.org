''' tests the functionality of the shapes.Circle class '''

import math
import pytest
from src import shapes
from typing import Callable

class TestCircle:
    
    def setup_method(self, method : Callable) -> None :
        self.circle = shapes.Circle(radius=10)
        
    def teardown_method(self, method : Callable) -> None :
        pass
        
    def test_area(self) -> None :
        assert self.circle.area() == (math.pi * self.circle.radius ** 2)
        
    def test_perimeter(self) -> None :
        assert self.circle.perimeter() == (math.pi * self.circle.radius * 2)
        
    def test_not_same_area_rectangle(
        self, 
        my_rectangle : shapes.Rectangle
    ) -> None :
        assert self.circle.area() != my_rectangle.area()