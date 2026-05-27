#Angelina and Sophia
#POKEMON GAME
level = 0
day = 1
name = "Gastly"
import random

#Functions
def gastly():
    print((r"                            _\n"))
    print((r"                         .\"' `..._\n"))
    print((r"                        '         `.\n"))
    print((r"                      .'      ___..'\n"))
    print((r"                _   .\"       '   .__,-.,\"\", ,----.\n"))
    print((r"     ,.-\"\"''-..\" :  :        `--'        ' :      :\n"))
    print((r"   .'            :_,'                    `._`\"--. ;\n"))
    print((r"   :              _,.--'\"'\"\"`--._           `.  `\"\n"))
    print((r"  j             ,'               `-.      ,._.'  ,\"\".\n"))
    print((r"  :           ,'                   ,-.   .   __  `..'\n"))
    print((r"  `--.    .'.'                   ,'   `. :_,\"  `.\n"))
    print((r",.   ;   .   \\                 ,'      |         `.\n"))
    print(("' :  :    |    `.             ,'        |\\         `.  _\n"))
    print((r"`.   ._  |      \\         _.'          | .      ___ `\" :\n"))
    print((r"       : '     . \\      ,'  .          ' |     :   `...'\n"))
    print((r"      ,'  \\       `.   .             ,'  |     '  __\n"))
    print((r"     .    `.       |    \\          .'    '    .  (  `.\n"))
    print((r"   .'      \\`.___,'      `-.____.-'     '     :   `-.'\n"))
    print((r"    .   ,\". \\ ..___              _     /      :    .\n"))
    print((r"    :   . :  \\|/\\  `\"'--------+\"|,'  ,'       `-..' :\n"))
    print((r"     `-\" .'   `: `\"-.._______,.\\|  .'               '\n"))
    print((r"         `--. _ `._             _,'        ,\"\"-.__,'\n"))
    print((r"             \" :   `\"--.....--\"'     __   .\n"))
    print((r"             ,-'                 ,.-\"  `-'\n"))
    print((r"            :   ,..             .    ,\"\".\n"))
    print((r"           .'   .  :   __..._   `\"-. :   :\n"))
    print((r"           `.._  : ' ,'      `\"--..' `--\"\n"))
    print((r"               `-' `\" mh\n"))
def haunter():
    print((r"              -._                                   _.\n"))
    print((r"               \\ `-.._                           _,' |\n"))
    print((r"                \\     `-._    _,.--------.._  _.\"    '\n"))
    print((r"                 \\        `--'              ``.     /\n"))
    print((r"                  \\                                j    __\n"))
    print(("__         __       \\                               |.-\"' /\n"))
    print((r"`.`-.`-.__`.`'\"----\"\\                              |    /\n"))
    print((r"   `.       `.       '        ._                       /\n"))
    print((r"   `..        \\               | `.               /|   /\n"))
    print((r"     `.        `.             |   `._          .' |  /\n"))
    print((r"       `.  .-----`            |      `.       /   ' '\"\"''\n"))
    print((r"         `. `.            .    ._      `_    /  ,'    .'\n"))
    print((r"           `. `.           `._   `'\"\"'\"'     \"\"' ,  ,'\n"))
    print((r"             `. `.          `.`.              ,-/ ,'       _..\n"))
    print((r"               `. `.          \\|,---..  ,--\"./ / ,--------\".  \\\n"))
    print((r"                 `._           `.     `/ , .`.',:           \\  \\\n"))
    print((r"                    `._          `..\".,./ ' _.' :            \\  `.\n"))
    print((r"                  ,-'\" `-._              _.\"     .   |.-\"`.   \\  |\n"))
    print((r"                 .         `-..........-'        |   `..   \\   |_'\n"))
    print((r"                 |           `\".                 `.._   .  '  ,'\n"))
    print((r"                 |         |   |                     `\"'    .'\n"))
    print((r"                 |   /\\    |'  '\n"))
    print((r"                 '  /  \\   ||   .\n"))
    print((r"                '   \\  '   |'   ;\n"))
    print((r"                 \\  '  \\   `...'\n"))
    print((r"                  `\"\"   `,' mh\n"))
def gengar():
    print((r"                |`._         |\\\n"))
    print((r"                `   `.  .    | `.    |`.\n"))
    print((r"                 .    `.|`-. |   `-..'  \\           _,.-'\n"))
    print((r"                 '      `-. `.           \\ /|   _,-'   /\n"))
    print((r"             .--..'        `._`           ` |.-'      /\n"))
    print((r"              \\   |                                  /\n"))
    print((r"           ,..'   '                                 /\n"))
    print((r"           `.                                      /\n"))
    print((r"           _`.---                                 /\n"))
    print((r"       _,-'               `.                 ,-  /\"-._\n"))
    print((r"     ,\"                   | `.             ,'|   `    `.\n"))
    print((r"   .'                     |   `.         .'  |    .     `.\n"))
    print((r" ,'                       '   ()`.     ,'()  '    |       `.\n"))
    print(("'-.                    |`.  `.....-'    -----' _   |         .\n"))
    print((r"/ ,   ________..'     '  `-._              _.'/   |         :\n"))
    print((r"` '-\"\" _,.--\"'         \\   | `\"+--......-+' //   j `\"--.. , '\n"))
    print((r"   `.'\"    .'           `. |   |     |   / //    .       ` '\n"))
    print((r"     `.   /               `'   |    j   /,.'     '\n"))
    print((r"       \\ /                  `-.|_   |_.-'       /\\\n"))
    print((r"        /                        `\"\"          .'  \\\n"))
    print((r"       j                                           .\n"))
    print((r"       |                                 _,        |\n"))
    print((r"       |             ,^._            _.-\"          '\n"))
    print((r"       |          _.'    `'\"\"`----`\"'   `._       '\n"))
    print((r"       j__     _,'                         `-.'-.\"`\n"))
    print((r"         ',-.,' mh\n"))


def main():
    print ("Welcome!")
    while True:
        global day
        print ("It is day " + str(day) + ", what would you like to do?: ")
        option = input ("train, evolve, info, battle, final boss, exit: ")
        if option == "info":
            info()
            day = day + 1
        if option == "train":
            train()
            day = day + 1
        if option == "battle":
            battle()
        if option == "final boss":
            final_boss()
        if option == "exit":
            break
    print (" ")

def info():
    global name
    global level
    print (" ")
    print ("Name: " + str(name))
    print ("Level: " + str(level))
    if level <= 10:
        print (gastly())
    if 10 < level < 20:
        print (haunter())
        name = "Haunter"
    if level >= 20:
        print (gengar())
        name = "Gengar"
    print (" ")

def evolve():
    global level
    global name
    if level <= 10:
        name = "Gastly"
    if 10 < level < 20:
        name = "Haunter"
    if level >= 20:
        name = "Gengar"

def train():
    global level
    print (str(name) + " just ran 10 laps.")
    level = level + 1
    print (" ")

def battle():
    global name
    global level
    global day
    print (" ")
    print ("Welcome to the ultimate Pokemon Gym Arena!")
    while True:
        print ("You are now battling trainer Sofia and Charizard.")
        rate = random.randint(0, 100)
        if rate >= 60:
            print ("You lost! Better luck next time.")
            continue
        if rate < 60:
            print ("You won! " + str(name) + " just leveled up two times.")
            print (" ")
            print (" ")
            level = level + 2
            break
    while True:
        print ("You are now battling trainer Angelina and Snorlax.")
        rate = random.randint(0, 100)
        if rate >= 60:
            print ("You lost! Better luck next time.")
            continue
        if rate < 60:
            print ("You won! " + str(name) + " just leveled up two times.")
            print (" ")
            print (" ")
            level = level + 2
            break
    day = day + 1

def final_boss():
    global name
    global level
    global day
    day = day + 1
    print ("You are at the final boss! You are facing Pikachu.")
    print (" ")
    bossrate = random.randint(0,100)
    if bossrate >= 60:
        print ("You lost!  " + str(name) + " has died. The game has been restarted.")
        print (" ")
        day = (day + 1) - day
        level = (level + 1) - level
        name = "Gastly"
    if bossrate < 60:
        print ("You won and completed the game! The game is now restarting.")
        print (" ")
        day = (day + 1) - day
        level = (level + 1) - level
        name = "Gastly"


#main
main()
