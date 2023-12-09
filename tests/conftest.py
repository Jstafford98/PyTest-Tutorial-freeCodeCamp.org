''' configures testing objects globally '''

import pytest
from src import shapes

@pytest.fixture
def my_rectangle() -> shapes.Rectangle :
    return shapes.Rectangle(length=10, width=20)

@pytest.fixture
def weird_rectangle() -> shapes.Rectangle :
    return shapes.Rectangle(length=5, width=6)