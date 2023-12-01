class A:
    def method(self):
        print("Method of class A")

class B(A):
    def method(self):
        print("Method of class B")

class C(A):
    def method(self):
        print("Method of class C")

class D(B, C):
    pass

print(D.mro())

d_obj = D()

d_obj.method()
