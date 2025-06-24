class A:
    def __init__(self,name,age):
        #private member
        self.__name=name
        #Procted member
        self._age=age
    def greet(self):
        print("Good Morning from A ")
class B(A):
    def display(self):
        print(self._age)
        print(self.__name)
# objA=A('qwert',23)
# objA.greet()
objB=B('qwert',23)
objB.display()