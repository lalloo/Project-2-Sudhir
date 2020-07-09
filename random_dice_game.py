#develop random no
#check the no
#print the face
#looping

import random
print("Welcome to the master dice simulator")
x = "y"

while x =="y":
    number = random.randint(1, 6)
    if number == 1:
        print(" ________")
        print("|        |")
        print("|   0    |")
        print("|________|")

    if number == 2:
        print(" ________")
        print("|        |")
        print("|0     0 |")
        print("|________|")

    if number == 3:
        print(" ________")
        print("|   0    |")
        print("|   0    |")
        print("|___0____|")

    if number == 4:
        print(" ________")
        print("|0      0|")
        print("|        |")
        print("|0______0|")

    if number == 5:
        print(" ________")
        print("|0      0|")
        print("|   0    |")
        print("|0______0|")

    if number == 6:
        print(" ________")
        print("|0      0|")
        print("|0      0|")
        print("|0______0|")
    x = input("Play again y or n")
    if x == "n":
        print("Game over")
