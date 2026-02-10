#Custom Exception Classes
class AppError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        
class InsufficientFundsError(AppError):
    pass
def withdraw(balance,amount):
     if balance < amount:
        raise InsufficientFundsError("Balance is not enogh")
     return balance - amount
 
class InvalidAgeError(AppError):
    pass
def age_validation(age):
     if age < 18:
        raise InvalidAgeError("Age is not valid") 
     return "Registration is successfully"

class DuplicateEntryError(AppError):
    pass
def user_data(name):
     if name in user:
        raise DuplicateEntryError("Name already exists")
     else:
        user.append(name)
        return "User add successfully"
user = ['Mahima','Rahul']

print ("-----Balance check Test-----")
try:
    print(withdraw(5000,9000))
except InsufficientFundsError as e:
    print("Error:",e.message)
    
print("\n---- Age Test ----")
try:
    print(age_validation(12))
except InvalidAgeError as e:
    print("Error:",e)


print("\n---- Duplicate User Test ----")
try:
    print(user_data("Rahul"))
except DuplicateEntryError as e:
    print("Error:",e) 