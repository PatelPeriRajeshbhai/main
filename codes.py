#1
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
print("Circle Area:",circle.area())
print("Circle Perimeter:",circle.perimeter())
print("Rectangle Area:",rectangle.area())
print("Rectangle Perimeter:",rectangle.perimeter())

#2
def word_break(s,words):
    temp = ''
    for ch in s:
       temp += ch
    if temp in words:
            temp = ""
    return temp == ""
print(word_break("helloword",["hellow","word"]))

#3
def edit_distance(word1,word2):
    count = abs(len(word1) - len(word2))
    for i in range(min(len(word1),len(word2))):
        if word1[i] != word2[i]:
            count += 1
#4
def can_partition(num):
    total = sum(num)
    return total % 2 == 0
print(can_partition([1,5,12,5]))

#5
def pali_sub(s):
    rev = s[::-1]
    count = 0 
    for i in range(len(s)):
        if s[i] == rev [i]:
            count += 1
    return count
print(pali_sub("aabaa"))

#6
def long_chain(p):
    p.sort()
    count = 1
    for i in range(1,len(p)):
        if p[i][0] > p[i-1][1]:
            count +=1
    return count
print(long_chain([[2,3],[1,2],[3,4]]))

#7
eggs = 2
floors = 10
def min_drops(e,f):
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f

    res = float('inf')
    for x in range(1,f+1):
        res = min(res,1 + max(min_drops(e-1,x-1), min_drops(e,f-x)))
    return res

print(min_drops(eggs,floors))

#8
def trap_water(h):
    water = 0
    for i in range(1, len(h)-1):
        left = max(h[:i])
        right = max(h[i+1:])
        water += max(0,min(left,right)-h[i])
    return water

#9
class MyString:
    def __init__(self,text):
        self.text = text
    def __add__(self,other):
        return MyString (self.text + other.text)
    def __mul__(self, n):
        return MyString(self.text * n)
    def __str__(self):
        return self.text
    
s1 = MyString("Hello")
s2 = MyString("Bye")
print(s1 + s2)
print(s1 * 3)     

#10
class Calculator:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        if b == 0:
           return "Error! Division by zero"
        return a / b
calc = Calculator()
print(calc.add(5,3))      
print(calc.subtract(10,4))      
print(calc.multiply(3,7))       
print(calc.divide(10,2))

#11 
arr = [
    [3, 5, 9],
    [1, 6, 7],
    [4, 8, 2]
]
temp = 1
econd = 1

for row in arr:
    for num in row:
        if num > temp:
          second = temp
          temp = num
        elif num >second and num != temp:
            second = num
print("Maximum:",temp)
print("Second Maximum:",second)

#12
class MyClass:
    def show(self, value):
        if type(value) == int:
            print("Integer:", value)
        elif type(value) == float:
            print("Float:", value)
        elif type(value) == str:
            print("String:", value)
        else:
            print("Other type:", value)
a = MyClass()
a.show(10)      
a.show(3.14)    
a.show("Hello")

#13
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
class Bird(Animal):
    def make_sound(self):
        print("chirps!")
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.make_sound()
    
#14
sales = {
    "Apple": [100,200,150],
    "Banana": [80,120],
    "Orange": [90,110,130]
}
total_sales = {}
for product in sales:
  total_sales[product]= sum(sales[product])
  
print(total_sales)  

#15
def make_chunks(lst,size):
    chunks = []
    for i in range(0,len(lst),size):
        chunks.append(lst[i:i+size])
    return chunks
numbers = [1, 2, 3, 4, 5, 6, 7]
print(make_chunks(numbers, 3))

#16
t = (2,3,4,5)
tup_new =(2)

tup_new = t * tup_new
print(tup_new)

#17
def top_students(students):
    result = {}
    for name,score in students.items():
        if score > 90:
            result[name] = score
    return result
students = {
    "Sita": 85,
    "Riya": 92,
    "Karan": 78,
    "Vina": 95
}
print(top_students(students))

#18
def flatten_list(nested):
    flat = []
    for i in nested:
        if type(i) == list:
            for x in i:
                flat.append(x)
        else:
            flat.append(i)
    return flat
data = [1,[2,3],[4,5],6]
print(flatten_list(data))

#19
favorite_foods = ("Pizza", "Burger", "Pasta")
def get_foods(*foods):
    return foods
print(get_foods("Pizza", "Ice Cream", "Sandwich"))

#20
library = {
    "Fiction": {
        "Harry Potter": "J.K. Rowling",
        "The Alchemist": "Paulo Coelho"
    },
    "Non-fiction": {
        "Sapiens": "Yuval Noah Harari",
        "Atomic Habits": "James Clear"
    }
}
print(library)



 


