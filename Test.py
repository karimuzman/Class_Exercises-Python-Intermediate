import pytest
from Exercises_Class09 import get_circle_area
from Exercises_Class09 import get_circle_circumference

def test_get_circle_area_positive_radius():
    radius = 3
    expected_area  = 28.27
    calculated_area = round((get_circle_area(radius)), 2)
    assert calculated_area == expected_area

def test_get_circle_area_negative_radius():
    radius = -1
    with pytest.raises(ValueError):
        get_circle_area(radius)

def test_get_circle_circumference_positive():
    radius = 3
    expected_circumference  = 18.85
    calculated_circumference = round((get_circle_circumference(radius)), 2)
    assert calculated_circumference == expected_circumference

def test_get_circle_circumference_negative():
    radius = -1
    with pytest.raises(ValueError):
        get_circle_circumference(radius)
