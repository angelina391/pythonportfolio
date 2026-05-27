#Angelina Huang
#Dog Breed
#The purpose of my program is to help users choose a dog breed that meets their needs
#Initialize
import pandas as pd

data = pd.read_csv('dog.csv')
minweight = data['Minimum Weight'].tolist()
maxweight = data['Maximum Weight'].tolist()
breed = data['Breed Group'].tolist()
name = data['Name'].tolist()
id = data['id'].tolist()
bredfor = data['BredFor'].tolist()
maxheight = data['Maximum Height'].tolist()
minheight = data['Minimum Height'].tolist()
temp = data['Temperament'].tolist()
image = data['Image'].tolist()

filter = []

#Functions
def menu():
    while True:
        information = input("Welcome! Do you want a specific size, dog breed, or purpose? (type exit to leave): ")
        if information == "size":
            choice1 = input("What size?: ")
            dogsize(choice1)
            continue
        if information == "dog breed":
            choice2 = input("What breed?: ")
            info(choice2)
            continue
        if information == "purpose":
            choice3 = input("What purpose? :")
            specify(choice3)
            continue
        if information == "exit":
            break

def dogsize(size):
    if size == "tiny":
        for i in range(len(minweight)):
            if minweight[i] <= 10:
                filter.append(name[i])
    if size == "small":
        for i in range (len(minweight)):
            if minweight[i] > 11 and minweight[i] < 25:
                filter.append(name[i])
    if size == "medium":
        for i in range (len(minweight)):
            if minweight[i] > 26 and minweight[i] < 60:
                filter.append(name[i])
    if size == "large":
        for i in range (len(minweight)):
            if minweight[i] > 60:
                filter.append(name[i])
    print(filter)
    filter.clear()

def info(breed_name):
    for i in range(len(breed)):
        if breed_name in breed[i]:
            filter.append (temp[i])
            print (filter)
            filter.clear()
            filter.append (image[i])
            print (filter)
            filter.clear()
            filter.append (id[i])
            print (filter)
            filter.clear()

def specify(purpose):
    for i in range(len(breed)):
        if purpose in bredfor[i]:
            filter.append(name[i])
    print (filter)
    filter.clear()

#Main
menu()

#Sources
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
