#Angelina Huang
#Init
import pandas as pd

data = pd.read_csv('hacker.csv')

log_id = data['Log_ID'].tolist()
ip_address = data['IP_Address'].tolist()
protocol = data['Protocol'].tolist()
data_kb = data['Data_KB'].tolist()
time = data['Time'].tolist()
description = data['Description'].tolist()

person = []

moment = []
data = []
name = []

user_amount = []

#Functions
def user(word):
    for i in range(len(time)):
        if word in description[i]:
            person.append(log_id[i])
    print (person)
    print ("admin_backup")
    person.clear()

def stolendata(amount):
    for i in range (len(time)):
        if data_kb [i] > amount:
            moment.append(time[i])
            data.append(data_kb[i])
            name.append(log_id[i])
    print (moment)
    print(data)
    print(name)
    moment.clear()
    data.clear()
    name.clear()

def password(word):
    for i in range (len(time)):
        if word in description [i]:
            user_amount.append([i])
    print(len(user_amount))
    user_amount.clear()


#Main
password("Reset")

