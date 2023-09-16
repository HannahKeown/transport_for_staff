# a system asking people how they get to work, whether its by bike, car, train, etc 
# options : car, bicycle, bus, train, walk, train and bus

# -----------------------------------------------------------------------------------------

# imports 
import time
from tabulate import tabulate

# -----------------------------------------------------------------------------------------

# variables 
car = 0
bicycle = 0 
bus = 0 
train = 0 
walk = 0
train_and_bus = 0 
staff_members = 0 

# -----------------------------------------------------------------------------------------

while staff_members < 2: # edit this number for how many employees you have 

    name = input("What is your name: ")
    role = input("What is your job role: ")
    staff_members += 1

    print("##############################################################")
    print("Look at the following options, which ones do you take to work")
    print("                    # # # Car # # #")
    print("                    # # Bicycle # #")
    print("                    # # # Bus # # #")
    print("                     # # Train # # ")
    print("                    # # # Walk # # #")
    print("                   # Train and bus #")
    print("##############################################################")
    time.sleep(1.5)
    asking_staff = input("          Which method of transport do you take: ")

# -----------------------------------------------------------------------------------------

# if statements for the modes of transport 

    staff = asking_staff.lower()
    if staff == "car":
      car += 1
    elif staff == "bicycle":
       bicycle += 1
    elif staff == "bus":
     bus += 1
    elif staff == "train":
       train += 1
    elif staff == "walk":
      walk =+ 1
    elif staff == "train and bus" or "bus and train":
     train_and_bus += 1
    else:
       print("Option not available")

    continue

# -----------------------------------------------------------------------------------------

# outputs and shows how many staff members use each transport 

print("Here is how many staff members use each transport")

# assigning data 
data = [
        ["Car", car],
        ["Bicycle", bicycle],
        ["Bus", bus],
        ["Train", train],
        ["Walk", walk],
        ["Train and bus", train_and_bus]
        ]

headers = ["Mode of transport", "Number of staff"]


print(tabulate(data, headers=headers, tablefmt="grid"))


    