#Exponential Backoff
#Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting sfrom 1 second, but stops after 5 retries.
import time

name = "Khizar Hijazi"
wait_time = 1 
max_tries = 5 
attempts = 0

while attempts < max_tries:
    user_input = input("Enter your correct name: ").title()
    
    if user_input == name:
        print("Congratulations! You've entered the correct name.")
        break 
    else:
        print(f"Invalid name. This is your {attempts + 1} attempt. You have {max_tries - attempts - 1} attempts remaining.")
        time.sleep(wait_time) 
        wait_time *= 2 
        attempts += 1

if attempts == max_tries:
    print("Sorry, you've exceeded the maximum number of attempts.")


