class Person:
    #class attribute
    language="Python"
    def __init__(self,name,age):
        #instance attribute
        self.name=name
        self.age=age

    def display(self):
        print("Good Morning ",self.name,self.age)
        
objDharmishtha=Person("Dharmishtha",30)
objDharmishtha.display()
objDeep=Person("Deep",25)
objDeep.display()
