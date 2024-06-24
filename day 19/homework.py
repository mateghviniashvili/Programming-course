#List
item1 = ["school","home","work"]
item2 = ["friends", "cousins"]
item3 = ["fruit", "vegetable"]

#Indexing
Subject = [
    'English',
    'Science',
    'Art',
    'P.E',
]
choice = int(input("Enter the Subject number 0-3: "))

if choice in range(len(Subject)):
    print(Subject[choice])
else:
    False

Sports = [
    "Basketball",
    "Football",
    "Volleyball",
    "Tennis",
    "Judo",
]
choice = int(input("Enter Your Sports choice 0-4: "))
if choice in range(len(Sports)): 
    print(Sports[choice])
else:
    False

FootBall_Goats = [
    "Kvara",
    "Ronaldo",
    "Messi",
    "Neymar",
    "PELE",
    "MBappe",
    "Maradona",
]
choice = int(input("Enter your FootBall Goats choice o-6"))
if choice in range(len(FootBall_Goats)):
    print(FootBall_Goats[choice])
else:
    False