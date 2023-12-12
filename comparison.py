class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return (self.x ** 2 + self.y ** 2) > (other.x ** 2 + other.y ** 2)
point1 = Point(3, 4)
point2 = Point(3, 5)
print(point1 > point2)  

