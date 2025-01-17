# Q92) Create classes Rectangle and Square. Square should inherit from Rectangle (or implement composition) in a way that automatically sets the length and width to the same value.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def display(self):
        print(f"Rectangle - Length: {self.length}, Width: {self.width}, Area: {self.area()}, Perimeter: {self.perimeter()}")
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def display(self):
        print(f"Square - Side: {self.length}, Area: {self.area()}, Perimeter: {self.perimeter()}")
rectangle = Rectangle(5, 3)
rectangle.display()
square = Square(4)
square.display()
