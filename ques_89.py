# Q89) Modify the Car class to have default values for make and model if not provided.
class Car:
    def __init__(self, make="Unknown", model="Unknown", year=None):
        self.make = make
        self.model = model
        self.year = year
    def display_details(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year if self.year else 'Unknown'}")
car1 = Car(year=2020)
car2 = Car("Toyota", "Corolla", 2020)
car1.display_details()
car2.display_details()
