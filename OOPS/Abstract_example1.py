from abc import ABC,abstractmethod
class Bank(ABC):
    def __init__(self,amount):
        self.amount=amount
    def greet(self):
        print("Good Morning")
    @abstractmethod
    def calculateInterest(self):
        print("This is from abstract method")
class SBI(Bank):
    def calculateInterest(self):
        super().calculateInterest()
        return self.amount*0.20
class AXIS(Bank):
    def calculateInterest(self):
        return self.amount*0.05
class ICICI(Bank):
    def calculateInterest(self):
        super().calculateInterest()
        return self.amount*0.15
        

objSBI=SBI(1000)
objSBI.greet()
inter=objSBI.calculateInterest()
print(inter)
objAxis=AXIS(1000)
inter=objAxis.calculateInterest()
print(inter)
objICIC=ICICI(1000)
print(objICIC.calculateInterest())
