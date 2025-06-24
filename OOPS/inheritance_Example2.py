class Person:
    def __init__(self,name,address,c_no):
        self.name=name
        self.address=address
        self.c_no=c_no
class Employee(Person):
    def __init__(self, name, address, c_no,dept,salary):
        super().__init__(name, address, c_no)
        self.salary=salary
        self.dept=dept
    def display(self):
        print(self.name,self.address,self.c_no,self.dept,self.salary)
objE=Employee('Ram','Parimal',789089,'Software',123456)
objE.display()


        