## List
# Even number
number = [1,2,3,4,5,6,7,8,9]
even = []  
for i in number:
    if i % 2 == 0:  
        even.append(i)  
print(even)

#sort() use for decending order
a = ["Amit","Ram","Sita"]
a.sort(reverse=True)
print(a)

#comprehension
squre = []
for x in range(1,11):
    squre.append(x*x)
print(squre)


#find comman element in two list
a = [3,2,1,4,9,8]
b = [1,3,5,4]
c = []
for item in a:
 if item in b:  
  if item not in c: 
     c.append(item)
print(c)

#revers a number withoust revers method uses:
def reverse_list(lst):
    return lst [::-1]  
a = [1, 2, 3, 4, 5]
b = reverse_list(a)
print(b)

#unqiue valu find in two list
a = [3, 2, 1, 4, 9, 8]
b = [1, 3, 5, 4]
c = []
for num in a:
 if num not in b:  
   c.append(num)
for num in b:
    if num not in a:  
        c.append(num)
print(c)


