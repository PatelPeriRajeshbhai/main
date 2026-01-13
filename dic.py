##Dictionary
#find maximum soce 
student_score = {
    "Sita": 76,
     "Vijai": 87,
    "Rekha": 97
}
top_student = max(student_score,key=student_score.get)
print(top_student)


#comprehension
name = ["Rita","Rajesh"]
name_lenght = {name: len(name) for name in name}
print(name_lenght)


# use two dictionary
d1 = {
    "Amit": 1,
    "Ram": 2,
    "Ketan": 3
}

d2 = {
    "Ram": 4,
    "Ketan": 5,
    "Dhruv": 6
}

d3={}
for i in d1:
    d3[i] = d1[i]

for i in d2:
    if i in d3:
        d3[i] = [d3[i],d2[i]]
    else:
        d3[i]=d2[i]
print(d3)



#Product and Price
products = {
    "apple": 50,
    "banana": 20,
    "milk": 40,
    "bread": 30
}
product_name = input("Enter the product name:")

if product_name in products:
    print("Price:",products[product_name])
else:
    print("Sorry!Product not found.")


# key-value pair 
d1 = {"A": 1, "B": 2, "C": 3}
d2 = {"B": 2, "C": 4, "D": 3}
d3 = {}
for i in d1:
   if i in d2 and d1[i] == d2[i]:
        d3[i] = d1[i]  
print(d3)

