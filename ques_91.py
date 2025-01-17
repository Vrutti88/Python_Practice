# Q91) In the Dog class, override a method speak defined in Animal (e.g., Animal says “Some sound”, but Dog says “Woof!”).
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says Some sound.")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} says Woof!")
animal = Animal("Some Animal")
animal.speak()  
dog = Dog("Buddy", "Golden Retriever")
dog.speak() 
