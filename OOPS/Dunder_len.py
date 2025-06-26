class Person:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        return len(self.name)
    # def getLen(self):
    #     return len(self.name)
    
p1=Person("Dip")
print(len(p1))

p2=Person("Parth")
print(len(p2))