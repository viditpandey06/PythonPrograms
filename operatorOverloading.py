class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overloading addition (+) operator
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    # Overloading subtraction (-) operator
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    # Overloading multiplication (*) operator
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    # Overloading division (/) operator
    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)
    
    # Overloading string representation for printing
    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating instances of Vector2D
v1 = Vector2D(2, 3)
v2 = Vector2D(1, 4)

# Using overloaded operators
print("v1 + v2 =", v1 + v2)  # Output: (3, 7)
print("v1 - v2 =", v1 - v2)  # Output: (1, -1)
print("v1 * 2 =", v1 * 2)    # Output: (4, 6)
print("v2 / 2 =", v2 / 2)    # Output: (0.5, 2.0)
