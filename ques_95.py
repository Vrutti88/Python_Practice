# Q95) Create a class Counter with a class variable count. Implement a @classmethod to increment count and a @staticmethod to display some utility message.
class Counter:
    count = 0  
    @classmethod
    def increment(cls):
        cls.count += 1
        print(f"Count incremented to: {cls.count}")
    @staticmethod
    def display_message():
        print("This is a static method and does not depend on class or instance variables.")
Counter.increment()  
Counter.increment()  
Counter.display_message() 
