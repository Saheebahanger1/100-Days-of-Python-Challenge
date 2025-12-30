# Defining a Function in Python.
def my_function():
    print("Hello")
    print("Bye")

# Calling a function.
my_function()

# While Loops : (Until the condition is True it will run continously.)

# Check from 1 to 10 while no is even or odd?
num = 1
while num <= 10:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    num += 1  # Crucial to avoid infinite loop

# Hurdle 4 Game
# Link:- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Solving Code
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()        
    turn_right()
    move()
    turn_right()    
    while front_is_clear():
        move()    
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Final Project Day - 6 "Escaping The Maze "
# Link:- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Solving Code
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# The main loop continues until Reeborg reaches the goal
while not at_goal():
    if right_is_clear():
        # Priority 1: If the right side is open, turn right and move
        turn_right()
        move()
    elif front_is_clear():
        # Priority 2: If right is blocked but front is open, move straight
        move()
    else:
        # Priority 3: If both right and front are blocked, turn left
        turn_left()


