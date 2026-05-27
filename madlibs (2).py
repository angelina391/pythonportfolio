#angelina
#initialize
import random

#functions
def madlibs():
    #random feature
    randomday = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
    randomname = ["SOPHIA", "ANGELINA", "SOPHIE", "WINNIE"]
    randomrestaurant = ["MCDONALDS", "JOLLIEBEE", "BURGERKING", "WINGSTOP"]
    randomfood = ["HAMBURGER", "ICECREAM", "POTATO", "STEAK"]
    randommood = ["JOYFUL", "DEPRESSED", "ANNOYED", "ENERGETIC"]
    randomadj = ["GREAT", "HORRIBLE", "STINKY", "AMAZING"]
    randomplace = ["HOME", "TRAMPOLINE PARK", "WALMART", "TARGET"]
    randomact = ["CRAFTING", "COOKING", "DRAWING", "GAMING"]
    randomanimal = ["FOX", "BIRD", "RACCOON", "RAT"]
    randomnumber = ["31", "2", "3", "4", "5", "7", "10", "25", "16", "62", "76"]
    #gather input
    day = input("enter a day or random: ")
    if day == "random":
        day = random.choice(randomday)
    name = input("enter a name or random: ")
    if name == "random":
        name = random.choice(randomname)
    restaurant = input("enter a restaurant or random: ")
    if restaurant == "random":
        restaurant = random.choice(randomrestaurant)
    food = input("enter a food or random: ")
    if food == "random":
        food = random.choice(randomfood)
    mood1 =input("enter a mood or random: ")
    if mood1 == "random":
        mood1 = random.choice(randommood)
    mood2 =input("enter a mood or random: ")
    if mood2 == "random":
        mood2 = random.choice(randommood)
    adjective2 = input("enter an adjective or random: ")
    if adjective2 == "random":
        adjective2 = random.choice(randomadj)
    adjective3 = input("enter an adjective or random: ")
    if adjective3 == "random":
        adjective3 = random.choice(randomadj)
    adjective4 = input("enter an adjective or random: ")
    if adjective4 == "random":
        adjective4 = random.choice(randomadj)
    place =input("enter a place or random: ")
    if place == "random":
        place = random.choice(randomplace)
    activity =input("enter an activity or random: ")
    if activity == "random":
        activity2 = input("enter an activity or random: ")
    if activity2 == "random":
        activity2 = random.choice(randomact)
    number1 =input("enter a number or random: ")
    if number1 == "random":
        number1 = random.choice(randomnumber)
    number2=input("enter a number or random: ")
    if number2 == "random":
        number2 = random.choice(randomnumber)
    animal = input("enter an animal or random: ")
    if animal == "random":
        animal = random.choice(randomanimal)

    #story
    print (f"""On \033[1m{ day }\033[0m, I saw my friend \033[1m{name}\033[0m at \033[1m{restaurant}\033[0m. We decided to order together and we got some \033[1m{food}\033[0m. They were very \033[1m{mood1}\033[0m, but I was \033[1m{mood2}\033[0m. We ate for \033[1m{number1}\033[0m hours! After eating we were very \033[1m{adjective2}\033[0m and decided to go to \033[1m{place}\033[0m. On the way, we saw a \033[1m{adjective4}\033[0m \033[1m{animal}\033[0m. We then went \033[1m{activity} for \033[1m{number2}\033[0m hours. It was so \033[1m{adjective3}\033[0m. Finally, \033[1m{name}\033[0m went home and said bye and it was fun, but I wish we couldve \033[1m{activity2}\033[0m instead.""")

#main
madlibs()
