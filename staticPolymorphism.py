class Calculator:
    def add(self, *args):
        total = 0
        for num in args:
            total += num
        return total

# Creating an instance of the Calculator class
calc = Calculator()

# Calling the add method with different numbers of arguments
print("Addition with two arguments:", calc.add(5, 3))
print("Addition with three arguments:", calc.add(5, 3, 2))
