class Mathmetics:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x


a=Mathmetics(12)
b=Mathmetics(22)
a1=10
b1=20
print(a+b)

