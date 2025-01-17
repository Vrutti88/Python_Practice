# Q96) Implement a Python class that overloads the __str__ method to return a string representation of the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
p = Person("Vrutti", 20)
print(p)  
