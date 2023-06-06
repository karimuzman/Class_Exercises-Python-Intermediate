class Robot:
    material = 'Metal'

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

# Creation of robot
x = Robot('John', 2023)
y = Robot('Kevin', 2022)

# Access to the methods
x.say_hello()
y.say_hello()

# Access to attribute
print(x.year)
print(y.name)
