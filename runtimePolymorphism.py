class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function to demonstrate polymorphism
def animal_sound(animal):
    return animal.speak()

# Creating instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Demonstrating runtime polymorphism
print("Dog says:", animal_sound(dog))
print("Cat says:", animal_sound(cat))
print("Cow says:", animal_sound(cow))
