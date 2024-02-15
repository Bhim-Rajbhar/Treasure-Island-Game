print(
    
'''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
)

# Display introductory messages to the player
print("Welcome to Bhim's Treasure Island.")
print("Your mission is to find the treasure!")

# Prompt the player to make a choice at the beginning of the game
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

# Check the player's choice at the crossroad
if choice1 == "left":
    # If the player chooses "left"
    # Prompt the player to choose whether to wait for a boat or swim across the lake
    choice2 = input('You\'ve come to a lake. There is an island is the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()

    # Check the player's choice after reaching the island
    if choice2 == "wait":
        # If the player chooses to "wait"
        # Prompt the player to choose a door among three options: red, yellow, or blue
        choice3 = input("You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        
        # Check the player's choice of door
        if choice3 == "red":
            # If the player chooses the red door
            print("It's a room full of fire. Game Over.")
        elif choice3 =="blue":
            # If the player chooses the blue door
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "yellow":
            # If the player chooses the yellow door
            print("You found the treasure! You win!")
        else:
            # If the player chooses a door that doesn't exist
            print("You chose a door that doesn't exist. Game Over.")
    else:
        # If the player chooses to swim instead of waiting for a boat
        print("You got attacked by angry trout. Game Over.")

else:
    # If the player chooses "right" at the crossroad
    print("You fell into a hole. Game Over.")
