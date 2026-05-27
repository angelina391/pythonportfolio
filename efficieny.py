#Angelina Huang
import random
attempts = 0
# 1. Setup the game
secret_number = random.randint(1, 100)

#Function
def linear_search():
    global attempts
    for guess in range (1,101):
        if guess == secret_number:
            print(f"The Secret Number is: {secret_number}")
            print (f"attempts: {attempts}")
        elif guess != secret_number:
            attempts = attempts + 1


def binary_search():
    global attempts
    low = 1
    high = 100
    found = False
    while found == False:
        mid = (low + high) // 2
        if mid > secret_number:
            high = mid-1
            attempts = attempts + 1
        if mid < secret_number:
            low = mid + 1
            attempts = attempts + 1
        if mid == secret_number:
            found = True
    print(f"The Secret Number is: {secret_number}")
    print(f"attempts: {attempts}")

#Main
linear_search()



