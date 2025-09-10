#Random Module
import random

random_integer = random.randint(1 , 10)
print(random_integer)

#random floating No's between 0-10.
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# head or tails by random module
random_head_or_tail = random.randint(0,1)
if random_head_or_tail == 0:
    print("Heads")
else:
    print("Tails")

#Understanding the Offset and Appending Items to Lists.
#Lists[ , ]
India = ['J&k' , 'Delhi' , 'Maharashtra' , 'Assam']
print(India[0]) #indexing [0 to ... ,forward] or [-1 to ... ,backward]
India.append("kerala") #adding items to the list
print(India)

#Who will pay the Bill? Module
friends = ['Adeel' , 'Tawheed' , 'Haris' , 'Aasim' , 'Aadil']
print(random.choice(friends))

# Nested Lists
indoor_games = ['Chess' , 'Carrom' , 'Table Tennis' , 'Badminton']
outdoor_games = ['Cricket' , 'Football' , 'Hockey']
games = [indoor_games , outdoor_games]
print(games)

# Rock , Paper & Scissors Game.
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
#Getting User Input
user_choice = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.")
import random
#Generating the Computer's Choice
computer_choice = random.randint(0,2)
#Printing Choices for Debugging
print(f"Computer chose {computer_choice}")
#Handling Input Types and Validation
user_choice = int(user_choice)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose.")
#Organizing ASCII Art with Lists
game_images = [rock, paper, scissor]
if 0 <= user_choice <= 2:
    print("You chose:")
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])
#Determining the Outcome
if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose.")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("You lose.")
