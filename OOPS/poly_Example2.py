class Shape:
    def findArea(self):
        print("From Shape class")
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.legth=length
        self.width=width
    def findArea(self):
        #return super().findArea()
        return self.legth*self.width
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    def findArea(self):
        super().findArea()
        return 2*3.14*self.radius
obj=Rectangle(2,5)
print(obj.findArea())
obj1=Circle(2)
print(obj1.findArea())
