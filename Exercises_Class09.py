import math

def get_triangle_area(base, height):
    return base * height / 2

def get_square_area(side):
    return side * side


def get_rectangle_area(base, height):
    return base * height

def get_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

def get_circle_circumference(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius




