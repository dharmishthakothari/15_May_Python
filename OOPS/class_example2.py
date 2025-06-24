class Employee:
    countEmp=0
    def __init__(self,eid,name,address,dept,salary):
        self.name=name
        self.id=eid
        self.address=address
        self.dept=dept
        self.salary=salary
        Employee.countEmp+=1
    def display(self):
        print(self.id,"--->",self.name,"-->",self.address,"-->",self.dept,"-->",self.salary)
print(Employee.countEmp)
empRohit=Employee(101,'Rohit','Parimal','Software',20000)
empReena=Employee(102,'Reena','S.G. Highway','Desiging',21000)
print("No of Employee ",Employee.countEmp)
empParth=Employee(103,'Parth','Bopal','Admin',23000)
empRam=Employee(101,'Ram','Parimal','Software',26000)
empDiya=Employee(102,'Diya','S.G. Highway','Desiging',22000)
lst_employee=[empRohit,empReena,empParth,empDiya,empRam]
count=0
for i in lst_employee:
    i.display()
#     if i.dept=='Software':
#         count+=1
# print(count)
print(Employee.countEmp)

        