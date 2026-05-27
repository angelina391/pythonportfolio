#Angelina Huang
#Init
#Dataset with 12 numbers
dataset = [42,65,23,12,78,55,49,64,41,36,88,25,90]

#Loop that runs through list
def peaks():
    if dataset[0] > dataset [1]:
        print (f"Peak detected: Value {dataset[0]} at Index 0")
    if dataset [0] < dataset[1] > dataset [2]:
        print (f"Peak detected: Value {dataset[1]} at Index 1")
    if dataset [1] < dataset[2] > dataset [3]:
        print (f"Peak detected: Value {dataset[2]} at Index 2")
    if dataset [2] < dataset[3] > dataset [4]:
        print (f"Peak detected: Value {dataset[3]} at Index 3")
    if dataset [3] < dataset[4] > dataset [5]:
        print (f"Peak detected: Value {dataset[4]} at Index 4")
    if dataset [4] < dataset[5] > dataset [6]:
        print (f"Peak detected: Value {dataset[5]} at Index 5")
    if dataset [5] < dataset[6] > dataset [7]:
        print (f"Peak detected: Value {dataset[6]} at Index 6")
    if dataset [6] < dataset[7] > dataset [8]:
        print (f"Peak detected: Value {dataset[7]} at Index 7")
    if dataset [7] < dataset[8] > dataset [9]:
        print (f"Peak detected: Value {dataset[8]} at Index 8")
    if dataset [8] < dataset[9] > dataset [10]:
        print (f"Peak detected: Value {dataset[9]} at Index 9")
    if dataset [9] < dataset[10] > dataset [11]:
        print (f"Peak detected: Value {dataset[10]} at Index 10")
    if dataset [10] < dataset[11] > dataset [12]:
        print (f"Peak detected: Value {dataset[11]} at Index 11")
    if dataset[1] < dataset [12]:
        print (f"Peak detected: Value {dataset[12]} at Index 12")

#main
peaks()
