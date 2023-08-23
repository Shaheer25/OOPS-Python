from abc import ABC ,abstractmethod

class Shape(ABC):

    def area(self):
        pass

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius **2

class Rectangle:

    def __init__(self, width,height):
        self.width = width
        self.height=height

    def area(self):
        return self.width * self.height


circle= Circle(5)
rect=  Rectangle(4,5)

print(circle.area())
print(rect.area())
