class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator (+)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Method to display the point coordinates
    def display(self):
        print(f"({self.x}, {self.y})")

# Creating Point objects
point1 = Point(3, 4)
point2 = Point(1, 2)

# Adding two Point objects using the overloaded operator
result = point1 + point2

# Displaying the result of addition
print("Resultant Point:")
result.display()  # Output will be "(4, 6)"
