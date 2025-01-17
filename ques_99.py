# Q99) Create a class that uses the @property decorator to get/set an attribute with some validation logic.
class Temperature:
    def __init__(self, temp_celsius):
        self._temp_celsius = temp_celsius
    @property
    def temp_celsius(self):
        return self._temp_celsius
    @temp_celsius.setter
    def temp_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature can't be below absolute zero (-273.15°C).")
        self._temp_celsius = value
temp = Temperature(25) 
print(f"Temperature in Celsius: {temp.temp_celsius}")
temp.temp_celsius = 30  
print(f"Updated Temperature in Celsius: {temp.temp_celsius}")
try:
    temp.temp_celsius = -300  
except ValueError as e:
    print(e)  
