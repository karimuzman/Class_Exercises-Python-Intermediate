import math
import typing


class Shape:
    def area(self):
        raise NotImplementedError("area() method must be overridden by the child class")


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius


class Square(Rectangle):
    def __init__(self, length: float):
        super().__init__(length, length)


def area_sum(shapes: typing.List[Shape]):
    print(sum(s.area() for s in shapes))


_shapes = [Rectangle(2, 4), Square(3), Circle(10)]
area_sum(_shapes)
