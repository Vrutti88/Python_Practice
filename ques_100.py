# Q100) Demonstrate multiple inheritance with two parent classes providing different functionalities to a child class.
class Animal:
    def eat(self):
        print("This animal eats food.")
class Bird:
    def fly(self):
        print("This bird can fly.")
class Parrot(Animal, Bird):
    pass
parrot = Parrot()
parrot.eat()  
parrot.fly()  
