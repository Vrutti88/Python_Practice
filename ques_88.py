# Q88) Define a class Car with a constructor that sets make, model, and year. Create an instance and display its details.
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(f"Make is: {self.make} \nModel is: {self.model} \nYear is: {self.year}")
c=Car("Toyota","Corolla",2020)
c.display()
