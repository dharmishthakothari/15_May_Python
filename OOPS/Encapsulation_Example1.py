class Bank:
    def __init__(self,init_balance):
        self.__balance=init_balance
    def deposite(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance
    # def displayBalance(self):
    #     print("Your balance is ",self.__balance)
b1=Bank(10000)
print("Initial balance",b1.get_balance())
b1.deposite(2000)
print("After diposite ",b1.get_balance())
b1.withdraw(3000)
print("After Withdraw ",b1.get_balance())
b1.deposite(20000)
print("After diposite ",b1.get_balance())