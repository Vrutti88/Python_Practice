# Q90) Create a base class Animal and a derived class Dog. The Dog class should inherit attributes and methods from Animal.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def speak(self):
        print(f"{self.name} makes a sound.")
class Dog(Animal):
    def __init__(self, name, breed, species="Dog"):
        super().__init__(name, species)
        self.breed = breed
    def speak(self):
        print(f"{self.name} barks!")
animal = Animal("Some Animal", "Unknown Species")
animal.speak()
dog = Dog("Buddy", "Golden Retriever")
dog.speak()
print(f"{dog.name} is a {dog.breed} and is a {dog.species}.")
