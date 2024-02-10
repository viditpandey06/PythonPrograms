import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot compute square root of a negative number!"
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers!"
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Invalid input for logarithm!"
    else:
        return math.log(x, base)

def absolute_value(x):
    return abs(x)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")
print("7. Factorial")
print("8. Circle Area")
print("9. Circle Circumference")
print("10. Sine")
print("11. Cosine")
print("12. Tangent")
print("13. Logarithm")
print("14. Absolute Value")

while True:
    choice = input("Enter choice (1-14): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", exponentiate(num1, num2))
    elif choice in ('6', '7'):
        num = float(input("Enter the number: "))
        
        if choice == '6':
            print("Result:", square_root(num))
        elif choice == '7':
            print("Result:", factorial(int(num)))
    elif choice in ('8', '9'):
        radius = float(input("Enter the radius of the circle: "))
        
        if choice == '8':
            print("Area of the circle:", circle_area(radius))
        elif choice == '9':
            print("Circumference of the circle:", circle_circumference(radius))
    elif choice in ('10', '11', '12'):
        angle = float(input("Enter the angle in degrees: "))
        
        if choice == '10':
            print("Sine:", sine(angle))
        elif choice == '11':
            print("Cosine:", cosine(angle))
        elif choice == '12':
            print("Tangent:", tangent(angle))
    elif choice == '13':
        x = float(input("Enter the number: "))
        base = float(input("Enter the base for logarithm: "))
        print("Result:", logarithm(x, base))
    elif choice == '14':
        num = float(input("Enter the number: "))
        print("Absolute value:", absolute_value(num))
    else:
        print("Invalid input")

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        break
