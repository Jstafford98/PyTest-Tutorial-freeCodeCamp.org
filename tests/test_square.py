import pytest
from src import shapes

@pytest.mark.parametrize(
    "side_length, expected_area", 
    [
        (5, 25), 
        (4, 16), 
        (9, 81)
    ]
)
def test_multiple_square_areas(
    side_length : float, 
    expected_area : float
) -> None :
    assert shapes.Square(side_length=side_length).area() == expected_area
    
@pytest.mark.parametrize(
    "side_length, expected_perimeter",
    [
        (3, 12),
        (4, 16),
        (5, 20)
    ]
)
def test_multiple_perimeters(
    side_length : float, 
    expected_perimeter : float
) -> None :
    assert shapes.Square(side_length=side_length).perimeter() == expected_perimeter
    