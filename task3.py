class Account:
 def __init__(self,account_number,holder_name,balance):
    self.account_number = account_number
    self.holder_name = holder_name
    self.balance = balance
    
 def Deposit(self,amount):  
     self.balance += amount
     
 
 def Withdraw(self,amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
        print("Insufficient balance")
 
 def get_balance(self):
        print("Current Balance:", self.balance)       
 
class SavingsAccount(Account):
 def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

 def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        return interest    
        
        
class currentAccount(Account):
 def __init__(self, account_number,holder_name,balance,overdraft_limit):
          super().__init__(account_number,holder_name,balance)
          self.overdraft_limit = overdraft_limit
          
 def withdraw(self, amount):
             if amount <= self.balance + self.overdraft_limit:
              self.balance -= amount
              print("Withdraw successful (Overdraft allowed)")
             else:
               print("Overdraft limit exceeded")
               
s1 = SavingsAccount("SA101", "Ram", 10000, 5)
s1.Deposit(2000)
s1.Withdraw(3000)

interest = s1.calculate_interest()
print("Interest:", interest)

s1.get_balance()
print()

c1 = currentAccount("CA201", "Amit", 5000, 2000)
c1.withdraw(6000)
c1.get_balance()
