## Task 1: Recursion Fundamentals

### 1.1 Factorial Calculator
def factorial(n):
    if n < 0 :
        return "Error: factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(4))
print(factorial(0))
print(factorial(-2))

### 1.2 Fibonacci Series
def fibonaci(n,dp):
    if n  <= 1:
      return n
    if dp[n] != 1:
        return dp[n]
    dp[n] = fibonaci (n-1,dp) + fibonaci (n-2,dp)
    return dp[n]
def fibonaci(n):
    dp = [-1]*(n-1)
    return fibonaci(n,dp)
        
### 1.4 Nested Litst Flattener
def flatten_list(data):
    result = []
    for i in data:
        if isinstance(i,list):
            result += flatten_list(i)  
        else:
            result.append(i)           
    return result
data = [1,[2,3,[4,5]],6,[7,[8,9]]]
print(flatten_list(data))

## Task 2: Object-Oriented Programming (OOP)


