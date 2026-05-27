#Angelina Huang
#Initialize
#Periodic Table
import pandas as pd

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

filter = []

#Functions
def weight(num):
    for i in range(len(id)):
        if num < 20:
            filter.append(name[i])
        elif num < 91:
            filter.append(name[i])
        elif num > 91:
            filter.append(name[i])
        if num > 296:
            print("not found")
    print(filter)
    filter.clear()



#Main
weight(300)
