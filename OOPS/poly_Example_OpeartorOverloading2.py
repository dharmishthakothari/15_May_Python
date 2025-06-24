class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self,other):
        print(self.x*other.x,self.y*other.y)
        return self.x*other.x,self.y*other.y
    def __lt__(self,other):
        if self.x<other.x:
            return self.x
        else:
            return other.x
p1=Point(10,20)
p2=Point(5,2)
print(p1*p2)
print(p1<p2)