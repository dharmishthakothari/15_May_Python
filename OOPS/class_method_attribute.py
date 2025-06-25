class Person:
    greet="Good Morning Have a nice Day!!!"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
    @classmethod
    def sayHello(cls):
        cls.greet="Good Afternoon"
        print(cls.greet)
    @staticmethod
    def st_method():
        print("static method")

Person.sayHello()
p1=Person('qwert',20)

p2=Person('wert',20)
p3=Person('ert',20)
p2.display()
p1.display()
p3.display()

