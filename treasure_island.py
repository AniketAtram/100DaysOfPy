print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You have arrived at the crossroads. Which way would you like to go? type 'left' or 'right': ")

if direction.lower() == "left":
    swim_or_wait = input("You've arrived at a lake. Would you like to swim or wait for a while? type 'swim' or 'wait': ")
    if swim_or_wait.lower() == "wait":
        print("A boat arrives and safely takes you to the shore.")
        print("There are three doors in front of you. One red, blue and yellow")
        door = input("Which door do you want to enter? type 'red' or 'blue' or 'yellow': ")
        if door.lower() == 'yellow':
            print("You've found the treasure")
            print("You Won! Game over!")
        elif door.lower() == 'red':
            print("You got eaten alive by a giant spider!!")
            print("You Lost! Game over!")
        else:
            print("Grim reaper says hi! Time to go to hell!")
            print("Your greed has taken the best of you. Now spend eternity with Grim Reaper")
            print("You lost! Game over")
    else:
        print("You dived into the ocean and got swallowed by a large sea creature! Game over!")
else:
    print("Ohh No! You fell into a hole and died! Game over!")
