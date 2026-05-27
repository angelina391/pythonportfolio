#Angelina and Sophia's casino
#Init
slot = ["7", "🌟", "💝", "🌙", "❀", "♐", "♑", "♫", "✧", "💞", "💘", "🦎"]
import random
balance = 10000

#function
#slot machine
def casino():
    global balance
    while True:
        start = input("Spin the slot machine for 10 credits? (spin, cashout, or add): ")    #grab information
        if start == "spin":
            if balance >= 10:
                spin1 = random.choice(slot)
                print (spin1)
                spin2 = random.choice(slot)
                print (spin2)
                spin3 = random.choice(slot)
                print (spin3)
                if spin1 == "7" and spin2 == "7" and spin3 == "7":
                    print ("Jackpot!!!!!!!! You win $6,000!")
                    balance = balance - 10
                    balance = balance + 6000
                    print (f"Your balance: {balance}")
                elif spin1 == spin2 and spin2 == spin3:
                    print ("Small win!! $500 has been added to your balance!")
                    balance = balance - 10
                    balance = balance + 500
                    print (f"Your balance: {balance}")
                else:
                    print ("You lost!!")
                    balance = balance - 10
                    print (f"Your balance: {balance}")
            else:
                print ("INSUFFICIENT FUNDS. PLEASE INSERT CREDITS.")
        if start == "add":
            muhney = input("How much would you like to add? (10, 50, 100): ")
            if muhney == "10":
                balance = balance +10
                print (f"Your current balance: {balance}")
            if muhney == "50":
                balance = balance +50
                print (f"Your current balance: {balance}")
            if muhney == "100":
                balance = balance +100
                print (f"Your current balance: {balance}")
        if start == "cashout":
            print ("You have exited")
            break

#tester to see profits
def simulation():
    global balance
    for i in range(1000):
        spin1 = random.choice(slot)
        print (spin1)
        spin2 = random.choice(slot)
        print (spin2)
        spin3 = random.choice(slot)
        print (spin3)
        if spin1 == "7" and spin2 == "7" and spin3 == "7":
            print ("Jackpot!!!!!!!! You win $10,000!")
            balance = balance - 10
            balance = balance + 10000
        elif spin1 == spin2 and spin2 == spin3:
            print ("Small win!! $500 has been added to your balance!")
            balance = balance - 10
            balance = balance + 500
        else:
            print ("You lost!!")
            balance = balance - 10
    print (f"Total credits spent: 10000")
    print (f"Total credits earned: {balance}")
    print (f"Casino networth: {10000-balance}")

#wildcard for wins
def wildcard():
    global balance

#main
casino()
