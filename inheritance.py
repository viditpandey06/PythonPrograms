# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Single inheritance
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Multiple inheritance
class Cat(Animal, object):
    def meow(self):
        print(f"{self.name} is meowing.")

# Multilevel inheritance
class Puppy(Dog):
    def play(self):
        print(f"{self.name} is playing.")

# Hierarchical inheritance
class Lion(Animal):
    def roar(self):
        print(f"{self.name} is roaring.")

# Create objects and test inheritance
dog = Dog("Buddy")
dog.eat()
dog.bark()

cat = Cat("Whiskers")
cat.eat()
cat.meow()

puppy = Puppy("Max")
puppy.eat()
puppy.bark()
puppy.play()

lion = Lion("Simba")
lion.eat()
lion.roar()
