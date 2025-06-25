from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0
class Square(Shape):
    def area(self):
        return 4
sq=Square()
print(sq.area())
sh=Shape()
print(sh.area())