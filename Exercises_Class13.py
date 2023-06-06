class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.area = height*width

    @staticmethod
    def add_area (rectangle1, rectangle2):
        return rectangle1.area + rectangle2.area

x = Rectangle(2,4)
y = Rectangle(4,3)

print(Rectangle.add_area(x, y))
