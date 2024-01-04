class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Function to demonstrate polymorphism
def animal_sound(animal):
    animal.make_sound()

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the make_sound method using polymorphism
animal_sound(dog)  # Output will be "Woof!"
animal_sound(cat)  # Output will be "Meow!"
