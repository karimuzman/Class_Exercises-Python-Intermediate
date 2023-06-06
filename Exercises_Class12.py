class Student:
    # Class variable - a list to store all student instances
    all_students = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Add the newly created student instance to the all_students list
        Student.all_students.append(self)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


# Create a few student instances
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 24)

# Access the class variable all_students
print("List of all students:")
for student in Student.all_students:
    print(student)
