#1
#Create a base class Shape with methods to calculate area and perimeter. 
	#Derive classes Circle and Rectangle from it and override the methods.
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
circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

#9
# Create a custom string class that supports operator overloading for concatenation (+ operator) and replication (* operator). Demonstrate the usage of these overloaded operators.
# 	Explanation: This task involves creating a class with customized behavior for string concatenation and replication using operator overloading.
class MyString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("MyString must be initialized with a string")
        self.value = value
    def __add__(self, other):
        if isinstance(other, MyString):
            return MyString(self.value + other.value)
        elif isinstance(other, str):
            return MyString(self.value + other)
        else:
            raise ValueError("Can only concatenate with MyString or str")
    def __mul__(self, n):
        if isinstance(n, int):
            return MyString(self.value * n)
        else:
            raise ValueError("Can only multiply by an integer")
    def __str__(self):
        return self.value

    def __repr__(self):
        return f"MyString('{self.value}')"
s1 = MyString("Hello")
s2 = MyString("World")
s3 = s1 + " " + s2
print(s3)  
s4 = s1 * 3
print(s4)



#11
# Create a Calculator class with multiple methods for addition, subtraction, multiplication, and division. Implement method overloading to handle different parameter types (int, float, and possibly more). Demonstrate the usage of these overloaded methods.
# 	Explanation: This task challenges you to implement method overloading in a class with different parameter types and demonstrate its flexibility.
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
calc = Calculator()
print(calc.add(1, 2))             
print(calc.subtract(10, 4))       
print(calc.multiply(3, 5))     
print(calc.divide(10, 2))         

