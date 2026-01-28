#1
def reverse_string(s):
    reversed_s = ""
    for i in s:
        reversed_s = i + reversed_s
    return reversed_s
original_string = "hello world"
reversed_string = reverse_string(original_string)
print(f"Reversed: {reversed_string}")

#2
s = "Hello,World"
frequency = {}
for i in s:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] = 1
print(frequency)

#3
num = 132
num2 = str(num)
n = len(num2)
sum1 = 0
for i in num2:
    sum1 += int(i)**n 
if sum1 == num:
    print(num,"is an Armstrong number")
else:
    print(num,"is not Armstrong number")
    
#4
data1 = {'A':12,'B':25,'C':9}
data2 = {'a': 100, 'b': 200, 'c': 300}
for i in data2:
    if i in data1:
        data2[i] = data2[i] + data1[i]
print(data2)

#5
a =[[1, 2], [3, [4, 5]]] 
b = []
for sublist in a:
    for num in sublist:
        b.append(num)
print(b)

#6
res = []
for n in range(1,25):
    if n <= 1:
        continue 
    is_prime = True 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False  
            break
    if is_prime:
        res.append(n)  
print(res if res else "No")
            
#7
year = 2024
if  year % 400 == 0:
    print("leap year")
else:
    print("Not a leap year")
    
#8
s1 = "ring"
s2 = "ingr"
if len(s1) != len(s2):
    print ("No")
else:
    print("Yes")
print()

