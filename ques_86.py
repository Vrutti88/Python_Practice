# Q86) Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
person1 = Person("Vrutti", 20)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
