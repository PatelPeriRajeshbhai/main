import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2   
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(4,3,5)
print("Circle Area:",circle.area())
print("Circle Perimeter:",circle.perimeter())
print("Rectangle Area:",rectangle.area())
print("Rectangle Perimeter:",rectangle.perimeter())
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())