#Initialize
import random
draw = 0
loss = 0
win = 0
#functions
def rps():
    global draw
    global loss
    global win
    while True:     #to keep it going so the points add up
        value1 = random.randint(1,3)
        value2 = input ("rock, paper, or scissors? (or exit): ")
#all the draws
        if value1 == 2 and value2 == "paper":
            print ("It was a draw! draws: " + str(draw) + " losses: " + str(loss) + " wins: " + str(win))   #to show the points to the player
            draw = draw + 1
            continue
        elif value1 == 1 and value2 == "rock":
            print ("It was a draw! draws: " + str(draw) + ", losses: " + str(loss) + ", wins: " + str(win))
            draw = draw + 1
            continue
        elif value1 == 3 and value2 == "scissors":
            print ("It was a draw! draws: " + str(draw) + ", losses: " + str(loss) + ", wins: " + str(win))
            draw = draw + 1
            continue
#all the wins
        elif value1 == 1 and value2 == "paper":
            print ("You won! draws: " + str(draw) + ", losses: " + str(loss) + ", wins: " + str(win))
            win = win + 1
            continue
        elif value1 == 3 and value2 == "rock":
            print ("You won! draws: " + str(draw) + ", losses: " + str(loss) + ", wins: " + str(win))
            win = win + 1
            continue
        elif value1 == 2 and value2 == "scissors":
            print ("You won! draws: " + str(draw) + ", losses: " + str(loss) + ", wins: " + str(win))
            win = win + 1
            continue
#the losses
        elif value1 == 3 and value2 == "paper":
            print ("You lost! draws: " + str(draw) + ", losses: " + str(loss) + ", wins: " + str(win))
            loss = loss + 1
            continue
        elif value1 == 3 and value2 == "rock":
            print ("You lost! draws: " + str(draw) + ", losses: " + str(loss) + ", wins: " + str(win))
            loss = loss + 1
            continue
        elif value1 == 1 and value2 == "scissors":
            print ("You lost! draws: " + str(draw) + ", losses: " + str(loss) + ", wins: " + str(win))
            loss = loss + 1
            continue
#to leave the game
        elif value2 == "exit":
            break

#main
rps()
