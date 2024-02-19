class MyClass:
    def __init__(self):
        self.__private_var = 10
        self._protected_var = 20

    def __private_method(self):
        print("This is a private method")

    def _protected_method(self):
        print("This is a protected method")

    def public_method(self):
        print("This is a public method")
        self.__private_method()
        self._protected_method()


obj = MyClass()
obj.public_method()
print(obj._MyClass__private_var)
print(obj._protected_var)