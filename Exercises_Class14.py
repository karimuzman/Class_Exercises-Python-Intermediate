class Animal:
    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
    def print_info(self):
        print(f"Name: {self.name}, Category: {self.category}, Age: {self.age}")
class Mammal(Animal):
    def __init__(self, name, category, age, number_of_legs):
        super().__init__(name, category, age)
        self.number_of_legs = number_of_legs
        self.number_of_fins = 0
class Bird(Animal):
    def __init__(self, name, category, age, number_of_legs):
        super().__init__(name, category, age)
        self.number_of_legs = number_of_legs
        self.number_of_fins = 0
class Fish(Animal):
    def __init__(self, name, category, age, number_of_fins):
        super().__init__(name, category, age)
        self.number_of_fins = number_of_fins
        self.number_of_legs = 0
nemo = Fish("Nemo", "Fish", 2, 7)
bambi = Mammal("Bambi", "Mammal", 1, 4)
iago = Bird("Iago", "Bird", 4, 2)
nemo.print_info()
bambi.print_info()
iago.print_info()
animals = [
    Fish("Nemo", "Fish", 2, 7),
    Fish("Marti", "Fish", 2, 7),
    Mammal("Bambi", "Mammal", 1, 4),
    Mammal("Simba", "Mammal", 3, 4),
    Bird("Iago", "Bird", 4, 2),
]
total_legs = sum(animal.number_of_legs for animal in animals)
print(f"Total number of legs: {total_legs}")
categories = {"Mammal": 0, "Bird": 0, "Fish": 0}
for animal in animals:
    categories[animal.category] += 1
for category, count in categories.items():
    print(f"{category}s: {count}")

