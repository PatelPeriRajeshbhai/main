class Employee:
    def __init__(self,name,employee_id,__salary):
       self.name = name
       self.employee_id = employee_id
       self.__salary = __salary
       
    def salary_amount(self,amount):
        self.salary = amount
    
    def display_details(self):
        print("ID:",self.employee_id)
        print("Name:",self.name)
        print("Salary:",self.__salary) 
    def calculate_bonus(self):
        return self.__salary * 0.10 
        
class manager(Employee):
    def __init__(self, name, employee_id,__salary,team_members):
        super().__init__(name, employee_id,__salary)  
        self.team_members = team_members
        
    def calculate_bonus(self):
        return self.__salary* 0.10
   

class Developer(Employee):
    def __init__(self, name, employee_id, __salary,languages_list):
        super().__init__(name, employee_id, __salary)
        self.languages_list = languages_list
        
    def calculate_bonus(self):
        return self.__salary*0.15
   
    
m1 = manager(101,"Ram",50000,["Amit","Ravi"])
m1.display_details()
m1.calculate_bonus()
print("Bonus:", m1.calculate_bonus())
print()
d1 = Developer(201,"Shyam",40000,["Python","Java"])
d1.display_details()
d1.calculate_bonus()
print("Bonus:", d1.calculate_bonus())

    
