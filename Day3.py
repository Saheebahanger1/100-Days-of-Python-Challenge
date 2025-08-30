# Conditional Statements!

# Rollercoaster Ticket Counter.
print("Welcome to rollercoaster ride!")
height = int(input("What is your height in cm? "))
if height >= 120 : # if condition is true then print this line.
    print("You can go for a ride.")
else : # if condition is false then print this line.
    print("Sorry,you can't go for a ride.")


# Modulo Operator(%) :- gives remainder.
# Check wheather no. is even / odd
Number = int(input("Enter the no. you want to check : "))
if Number % 2 == 0 : #if remainder is zero then condition is true.
    print("The number is even.")
else:
    print("The number is odd.")


# Nested if statements and elif statements.
# Ticket Counter!
height = int(input("What is your height in cm? "))
if height >= 120 : # if condition is true then print this line.
    print("You can go for a ride.")
    age = int(input("What is your age : "))
    if age < 12: # nested if :- if inside another parent if.
        print("Ticket is free.")
    elif age <=18:
        print("Pay 20 Rupees.")
    else:
        print("Pay 40 Rupees.")
else:
    print("The number is odd.")

# Multiple if conditions.
# tickets counter!
age = int(input("What is your age : "))
bill = 0
if age < 12:
    bill = 10
    print("Pay 10 Rupees.")
elif age <=18:
    bill = 20
    print("Pay 20 Rupees.")
else:
    bill = 40
    print("Pay 40 Rupees.")
want_photos = input ("Do you want to have photos? Type y for Yes & n for No.")
if want_photos == "y":
    print("The total bill = " + str(bill + 5 ) + " Rupees.")
else:
    want_photos == "n"
    print("The total Bill = " + str(bill) + " Rupees.")


# Pizza Delivery Program!
print("Welcome to Pizza Corner!")
size = input("Which size of pizza do you Want? S , M or L.")
spicy = input("Do you want chilly flakes? Type y for Yes & n for No. ")
extra_cheese = input("Do you want extra cheese? Type y for Yes & n for No. ")
bill = 0

# Pricing Details
if size == "S":
    bill += 20
elif size == "M":
    bill += 40
elif size == "L":
    
    bill += 60
else:
     print("You entered wrong input.")

# Adding spice's Charges
if spicy == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Adding Extra Cheese Charge
if extra_cheese == "y":
    if size == "S":
         bill += 2
    else:
         bill += 5
print(f"Your final bill is equal to ,{bill} Rupees") 


# Logical Operators :- and,or,not.
# 1.AND :- Both statements must be True
# 2.OR :- One of the statement should be True
# 3.NOT :- if condition is True,it gives False & vice versa.
age = int(input("What is your age : "))
bill = 0
if age < 12:
    bill = 10
    print("Pay 10 Rupees.")
elif age <=18:
    bill = 20
    print("Pay 20 Rupees.")
elif age >= 40 and age <= 100:
    print("Ride is free.")
else:
    bill = 40
    print("Pay 40 Rupees.")


#Tresure Island Game!
print('''**********************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
stage_1 = input("you\'re at a cross road. " 
                "Where do you want to go? \n Type 'left' or 'right' ").lower()
if stage_1 == "left":
    stage_2 = input("You\'ve came to a lake. "
                    "There is an Island in the middle of the lake. "
                    "Type 'wait' to wait for the boat. Type 'swim' to swim across to the Island.").lower()
    if stage_2 == "wait":
        stage_3 = input("You arrived at the Island safely. There is a house with 3 doors."
                        "one yellow, one blue and one red"
                        "Which colour do you choose? ").lower()
        if stage_3 == "yellow":
            print("You found the tresure, You Win!")
        elif stage_3 == "Red":
            print("It's a room full of fire, Game Over")
        else:
            print("It's a room full of snakes, Game Over.")
    else:
        print("You got killed by an Alligator. Game Over")
else:
    print("You fell in to the hole. Game Over")



    

                                                      # <----------Day 3 Completed----------> #
