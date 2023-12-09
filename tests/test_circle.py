''' tests the functionality of the shapes.Circle class '''

import math
import pytest
from src import shapes

class TestCircle:
    
    def setup_method(self, method):
        self.circle = shapes.Circle(radius=10)
        
    def teardown_method(self, method):
        pass
        
    def test_area(self):
        assert self.circle.area() == (math.pi * self.circle.radius ** 2)
        
    def test_perimeter(self):
        assert self.circle.perimeter() == (math.pi * self.circle.radius * 2)