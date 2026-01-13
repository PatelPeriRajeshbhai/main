##TUPLE
#tuple into sparate variable
def person_det(name,age,city):
    print("Name:",name)
    print("Age:",age)
    print("City:",city)
person_det("Krishna",21,"Delhi")

#without duplicate element
tup1 = (8,4,2,3,9,12)
tup2 = (5,6,4,9,12)
result = []
for i in tup1:
    if i not in tup2:
        result.append(i)
for i in tup2:
    if i not in tup1:
        result.append(i)
print(result)


#faviort movies
faviort_movies = ("DDL","Stranger","Twlight","spider man","India")
print ("Fist two movie:",faviort_movies[:2])
print ("Last two movie:",faviort_movies[-2:])

#concatenate
fruit = ("apple","banana","mango")
numbers = (5,6,4,9,12)
color = ("red","yellow","blue")
print(fruit+numbers+color)

#information collect from user
name = input("Enter your name:")
age = input("Enter your age:")
city = input("Enter your city:")  
print("Your info:",(name,age,city))


#combine use zip()
names = ("Amit","Ram","Sita")
ages = (20,22,19)
combined = list(zip(names,ages))
print(combined)