class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        #p1.__gt__(p2)
        if self.age<other.age:
            return other
        else:
            return self
    def display(self):
        print(self.name,self.age)
p1=Person('Dharmishtha',30)
p2=Person('Person',40)
ans=p1>p2

ans.display()
        