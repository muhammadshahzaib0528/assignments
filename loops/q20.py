# Create a program that simulates a countdown timer starting from a given number down to zero.
import time 

def countdown_timer(start):
    for i in range(start, -1, -1):
        print(i)
        time.sleep(1) 
    print("Time's up!")
start_number = int(input("Enter the starting number for the countdown: "))
countdown_timer(start_number)
