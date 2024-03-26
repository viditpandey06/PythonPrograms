import copy

# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object
person1 = Person("John", 25)

# Perform deep copy
person2 = copy.deepcopy(person1)

# Modify the copied object
person2.name = "Alice"
person2.age = 30

# Display both objects
person1.display()
person2.display()