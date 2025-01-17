# Q117) Write a Python program that spawns two threads: one prints numbers 1 to 5, the other prints letters A to E.
import threading
import time
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(0.5)  
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(0.5)  
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both threads have finished execution.")
