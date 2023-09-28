"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, work, salary, hours, commissionType, commissionPay, contracts):
        #commissionTypes: 0 = none, 1 = static, 2 = contracts
        self.name = name
        self.work = work
        self.salary = salary
        self.hours = hours
        self.commissionType = commissionType
        self.commissionPay = commissionPay
        self.contracts = contracts

    def get_pay(self):
        if(self.work == "monthly" and self.commissionType == 0):
            return self.salary 
        elif(self.work == "hourly" and self.commissionType == 0):
            return self.salary * self.hours     
        #Monthly commission
        elif(self.work == "monthly" and self.commissionType != 0):
            if(self.commissionType == 1):
                return self.salary + self.commissionPay
            return self.salary + (self.commissionPay * self.contracts)
        #Hourly commission
        elif(self.work == "hourly" and self.commissionType != 0):
            if(self.commissionType == 1):
                return (self.salary * self.hours) + self.commissionPay
            return (self.salary * self.hours) + (self.commissionPay * self.contracts)

    def __str__(self):
        if(self.work == "monthly" and self.commissionType == 0):
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."
        elif(self.work == "hourly" and self.commissionType == 0):
            return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour. Their total pay is {self.get_pay()}." 
        elif(self.work == "monthly" and self.commissionType != 0):
            if(self.commissionType == 1):
                return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commissionPay}. Their total pay is {self.get_pay()}."
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commissionPay}/contract. Their total pay is {self.get_pay()}."
        elif(self.work == "hourly" and self.commissionType != 0):
            if(self.commissionType == 1):
                return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a bonus commission of {self.commissionPay}. Their total pay is {self.get_pay()}."
            return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a commission for {self.contracts} contract(s) at {self.commissionPay}/contract. Their total pay is {self.get_pay()}." 


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',"monthly",4000,0,0,0,0)
print(str(billie))
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"hourly",25,100,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',"monthly",3000,0,2,200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"hourly",25,150,2,220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',"monthly",2000,0,1,1500,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',"hourly",30,120,1,600,0)
