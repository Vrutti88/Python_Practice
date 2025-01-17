# Q98) Use the abc module to define an abstract base class Shape with an abstract method area(). Implement subclasses Circle and Rectangle.
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Area of Circle is: {circle.area()}")
print(f"Area of Rectangle is: {rectangle.area()}")
