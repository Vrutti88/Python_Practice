# Q93) Demonstrate encapsulation by creating a class with private attributes and use getter and setter methods to access/modify them.
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age 
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        if new_age > 0:  
            self.__age = new_age
        else:
            print("Age must be positive.")
person = Person("Alice", 25)
print("Name:", person.get_name())
print("Age:", person.get_age())
person.set_name("Bob")
person.set_age(30)
print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())
