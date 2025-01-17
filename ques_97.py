# Q97) Create a class Point that overloads the + operator (using __add__) to add the coordinates of two Point objects.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __str__(self):
        return f"({self.x}, {self.y})"
p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2  
print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Result of addition: {result}")
