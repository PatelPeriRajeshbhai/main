#1
def factorial (n):
 if n<=1:
     return n
 else:
     return n * factorial(n-1)
print (factorial(5))

#2
def sum_list(n):
    if len(n)==0:
       return 0
    else:
        return n [0] + sum_list(n[1:])
element_num = [1,2,4,5]
print(sum_list(element_num))

#3
def element_num(number):
    if len(number)==0:
        return 0
    else:
        return 1 + element_num(number[1:])
element_list=[1,2,3,4,5]
print(element_num(element_list))

#4
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return True
    else:
        return False
text = "River"
if is_palindrome(text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


#5  
def fizzbuzz(n):
  result = []
  for i in range(1,n + 1):
    if i % 3 == 0 and i % 5 == 0:
       print("FizzBuzz") 
    elif i % 3 == 0:
       print("Fizz")  
    elif i % 5 == 0:
       print("Buzz")
    else:
        print(fizzbuzz)
print(fizzbuzz(15)) 


#6
num = 12345
def findSum(num):
    if num == 0:
      return 0
    else:
     return int(num % 10) + findSum(num / 10)
print(findSum(num)) 

#7
def list_operations(lst):
    maximum = max(lst)             
    sorted_list = sorted(lst)      
    unique_list = []               
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return maximum, sorted_list, unique_list
numbers = [5, 2, 9, 2, 7, 5, 3]
max_val, sorted_numbers, unique_numbers = list_operations(numbers)
print("Maximum:",max_val)
print("Sorted list:",sorted_numbers)
print("Without duplicates:",unique_numbers)

#8
def leap_year(num):
    if num % 4 == 0:
      return True
    else:
        return False
print(leap_year(2025)) 

#9
number = (1,8,9,7) 
guess = int(input("Guess a number between 1 and 10: "))
if guess == number:
    print("You guessed it right!")
else:
    print("Wrong guess! The number was:", number)


        
    
 
