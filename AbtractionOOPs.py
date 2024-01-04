from abc import ABC, abstractmethod

# Creating an abstract class
class Shape(ABC):

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def calculate_area(self):
        pass

# Subclass of Shape (must implement the abstract method)
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    # Implementing the abstract method calculate_area for Square
    def calculate_area(self):
        return self.side_length ** 2

# Subclass of Shape (must implement the abstract method)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementing the abstract method calculate_area for Circle
    def calculate_area(self):
        return 3.14159 * self.radius ** 2

# Creating instances of Square and Circle
square = Square(5)
circle = Circle(3)

# Calculating and displaying the areas
print("Area of Square:", square.calculate_area())  # Output will be "Area of Square: 25"
print("Area of Circle:", circle.calculate_area())  # Output will be "Area of Circle: 28.27431"
