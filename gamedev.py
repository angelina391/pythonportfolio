#Angelina Huang
#init
import pandas as pd

data = pd.read_csv('gamedev.csv')

level = data['Level'].tolist()
time = data['Time'].tolist()
rating = data['Rating'].tolist()
summary = data['Summary'].tolist()
feedback = data['Feedback'].tolist()
filter = []

#Functions
def find_problems(level_rating):
    #STEP ONE: CREATE THE LOOP
    for i in range(len(rating)):
        #STEP TWO: CONDITIONAL STATEMENT
        if rating[i] < level_rating:
            #STEP THREE: ADD ITEMS TO THE FILTER
            filter.append([i])
    #STEP FOUR: Print filter and clear
    print (filter)
    filter.clear()

def find_good(level_rating, t):
    for i in range(len(rating)):
        if rating[i] > level_rating and time[i] > t:
            filter.append([i])
    print (filter)
    filter.clear()

def secret(word):
    for i in range(len(summary)):
        if word in feedback[i]:
            filter.append([i])
    print (filter)
    filter.clear()

#Main
secret("secret")
print (data.loc[66])
