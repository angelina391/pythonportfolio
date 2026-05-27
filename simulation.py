#Angelina Huang
tortoise_wins = 0
hare_wins = 0
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0		 #Starting Position
is_hare_asleep = False #Hare starts Awake
import random

#We need to keep track of the racer’s wins as the simulations runs
for i in range(100000):
    while tortoise_pos < finish_line and hare_pos < finish_line:
    # Tortoise always moves a short distance between 1 - 3 meters at random
        trandom = random.randint(1,3)
        tortoise_pos = tortoise_pos + trandom
        # Hare has a 30% chance of falling a sleep for a turn
        sleep_num = random.randint(1,100)
        if sleep_num <=81:
            hare_pos = hare_pos + 0
        # If Hare is awake, it will move 1 - 10 meters at random
        if sleep_num >= 81:
            hrandom = random.randint(1,10)
            hare_pos = hare_pos + hrandom
    if tortoise_pos >= finish_line:
            tortoise_wins = tortoise_wins + 1
    if hare_pos >= finish_line:
            hare_wins = hare_wins + 1
# Don’t forget to reset positions for EVERY new race
    tortoise_pos = 0
    hare_pos = 0

#Do not print the individual races anymore, instead print the results of 100,000 races
print(f"🐢 Tortoise Wins: {tortoise_wins}")
print(f"🐇 Hare Wins: {hare_wins}")
