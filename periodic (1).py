#Initialize
#The Element Identifier: provides assistance with the Periodic Table by giving a list of possible elements based on your input
import pandas as pd #for the csv file

#Create variables for information in csv file
data = pd.read_csv('periodic.csv')
id = data['id'].tolist()
period_number = data['Period Number'].tolist()
name = data['Name'].tolist()
symbol = data['Symbol'].tolist()
atomic_num = data['Atomic Number'].tolist()
atomic_weight = data['Atomic Weight'].tolist()
melting = data['Melting Point'].tolist()
boiling = data['Boiling Point'].tolist()
density = data['Density'].tolist()
phase = data['Phase at Room Temperature'].tolist()
classification = data['Atom Classification'].tolist()
group = data['Group'].tolist()
uses = data['Uses'].tolist()
#empty array as the filter
filter = []

#Functions
#INTRODUCTION MENU
def introduction():
    print ('\033[1m' +"Welcome! This program provides assistance with the Periodic Table by providing a list of possible elements based on your input." + '\033[0m')
    while True:
        start = input("Would you like to \033[36m(identify)\033[0m an element or get \033[36m(information)\033[0m about one? Enter \033[36m(quit)\033[0m to leave: ")  #gather input
        #IDENTIFY CATEGORY
        if start == "identify":
            one = input("Would you like to identify through atomic \033[36m(number, weight, phase\033[0m, or \033[36mclassification)\033[0m?: ")
            #Place Number function
            if one == "number":
                n = int(input("Please enter the atomic number: "))
                number(n)
            #Place Weight function
            elif one == "weight":
                minrange = int(input("Please enter the minimum weight you want: "))
                maxrange = int(input("Please enter the maximum weight you want: "))
                weight (minrange, maxrange)
            #Place Phase function
            elif one == "phase":
                p = input("Is your element's phase at room temperature \033[36m(Solid, Liquid,\033[0m or \033[36mGas)\033[0m?: ")
                phases(p)
            #Place Class function
            elif one == "classification":
                c = input("Please enter your element's class \033[36m(Metal, Non-metal, Semi-metal\033[0m, or \033[36mUnknown)\033[0m: ")
                classi(c)
            #If something else is being input
            elif one != "number" or "weight" or "phase" or "classification" or "group":
                print('\033[31m' + "Invalid. Please enter (number, weight, phase, or classification): " + '\033[0m')
                print(" ") #additional space to make the output look neater
            continue
        #INFORMATION CATEGORY
        elif start == "information":
            two = input("Do you want to know the \033[36m(general information)\033[0m of your element or something \033[36m(specific)\033[0m?: ") #gather input
            #general information function
            if two == "general information":
                e = input("What element would you like information for? (Please capitalize the first letter): ")
                general(e)
            elif two == "specific":
                ele = input("What specific aspect do you want? \033[36m(uses, melt/boiling point\033[0m, or \033[36mdensity)\033[0m: ")
            #Place Uses function
                if ele == "uses":
                    ask = input("What element do you want to know the uses of?: ")
                    use(ask)
            #Place Melt/boil function
                elif ele == "melt/boiling point":
                    ask = input("What element do you want to know the melting/boiling point of? Please capitalize the first letter: ")
                    melt_boil(ask)
            #Place Density function
                elif ele == "density":
                    ask = input("What element do you want to know the density of? Please capitalize the first letter: ")
                    dense(ask)
            #If something else is being input
                elif ele != "uses" or "melt/boiling point" or "density":
                    print ('\033[31m' + "Invalid. Please enter (uses, melt/boiling point, or density)." + '\033[0m')
                    print (" ")
            elif two != "general information" or "specific":
                print ('\033[31m' + "Invalid. Please enter (general information) or (specific)." + '\033[0m')
                print(" ")
            continue
        #EXIT CATEGORY
        elif start == "quit":
            print ('\033[1m' +"EXITING..." + '\033[0m')
            print ("Thank you, hope to see you next time!")
            print(" ")
            break
        #If something else is being input
        elif start != "information" or "identify" or "quit":
            print ('\033[31m' + "Invalid. Please input information, identify, or quit" + '\033[0m')
            print(" ")
            continue

#IDENTIFY CATEGORY
#Number function: find element based on atomic number
def number(num):
    for i in range(len(id)):
        if num == id[i]:
            filter.append(name[i])
    print('\033[32m' + "Possible elements: " + '\033[0m')
    print(filter)
    print (" ")
    filter.clear()

#Weight function: find element based on weight range
def weight(first, second):
    for i in range(len(id)):
        if first < atomic_weight[i] < second:
            filter.append(name[i])
    print('\033[32m' + "Possible elements: " + '\033[0m')
    print(filter)
    print (" ")
    filter.clear()

#Phase function: filter elements based on the phase
def phases(info):
    for i in range(len(id)):
        if info in phase[i]:
            filter.append(name[i])
    print('\033[32m' + "Possible elements: " + '\033[0m')
    print(filter)
    print (" ")
    filter.clear()

#Classification function: filter based on the classification given
def classi(cls):
    for i in range(len(id)):
        if cls in classification[i]:
            filter.append(name[i])
    print('\033[32m' + "Possible elements: " + '\033[0m')
    print(filter)
    print (" ")
    filter.clear()


#INFORMATION CATEGORY
#SUBCATEGORY - General info: find general information about a certain element
def general(elem):
    for i in range(len(id)):
        if elem in name[i]:
            print (" ")
            print ('\033[32m' + f"INFORMATION ON... {elem}: " + '\033[0m')
            print (f"Symbol: {symbol[i]}")
            print (f"Atomic Number: {density[i]}")
            print (f"Period: {period_number[i]}")
            print (f"Weight: {atomic_weight[i]}")
            print (f"Phase: {phase[i]}")
            print (f"Classification: {classification[i]}")
            print (f"Group: {group[i]}")
            print (" ")

#SUBCATEGORY - Specific
#uses function: find the uses of a certain element
def use(element):
    for i in range(len(id)):
        if element in name[i]:
            print ('\033[32m' + "Uses: " + '\033[0m')
            print(uses[i])
            print (" ")
#melting and boiling point function
def melt_boil(element):
    for i in range(len(id)):
        if element in name[i]:
            print ('\033[32m' + "Melting Point: " + '\033[0m')
            print(melting[i])
            print ('\033[32m' + "Boiling Point: " + '\033[0m')
            print(boiling[i])
            print (" ")
#density function: find the density of a certain element
def dense(element):
    for i in range(len(id)):
        if element in name[i]:
            print ('\033[32m' + "Density: " + '\033[0m')
            print (density[i])
            print (" ")

#Main
introduction()

#Sources
#The table used for this program: https://docs.google.com/spreadsheets/d/1Woc8Wkmj8OumNnRHy0_sFAJX1M7UsPMR8poz1C035-M/edit?gid=0#gid=0
#For the coloring of the text, this algorithm takes information from: https://jhkinfotech.medium.com/how-to-add-a-splash-of-color-to-your-console-output-52ade8cfe786
