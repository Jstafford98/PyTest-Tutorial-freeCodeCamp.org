''' Various shape objects '''

import math

class Shape:
    
    def area(self) -> None :
        pass
    
    def perimeter(self) -> None :
        pass
    
class Circle(Shape):
    
    def __init__(self, radius : float) -> None :
        self.radius = radius
        
    def area(self) -> float :
        return math.pi * self.radius**2
    
    def perimeter(self) -> float :
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    
    def __init__(self, length : float, width : float) -> None :
        self.length = length
        self.width = width
        
    def area(self) -> float : 
        return self.length * self.width
    
    def perimeter(self):
        return (self.length *2) + (self.width * 2)
    
    def __eq__(self, __value: object) -> bool:
        
        if not isinstance(__value, Rectangle):
            return False
        
        return self.width == __value.width and self.length == __value.length
    
class Square(Rectangle):
    
    def __init__(self, side_length : float) -> None :
        super().__init__(width=side_length, length=side_length)