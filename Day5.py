# For loop
fruits = ['Apple' , 'Peach' , 'Mango']
for fruit in fruits:
    print(fruit) #it will print each item one by one.

# Sum Functions.
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
total_exam_score = sum(student_scores)
print(total_exam_score)

# Sum using For Loop.
sum = 0
for score in student_scores:
    sum += score
print(sum)

# Max Number.
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
print(max(student_scores))

# Max Number Using For Loop.
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
max_num = 0
for score in student_scores:
    if score > max_num:
        max_num = score
print(max_num)

#For Loop using Range Funtion.
for num in range(1, 10):
    print(num)

# Adding No's from 1-100.
sum = 0
for num in range(1, 101):
    sum += num
print(sum)

# Py Password Generator.
import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "<", ">", "/", "?", "~", "`" ]

print("Welcome to the PyPassword Generator!")
req_letters = int(input("How many letters do you like in your password?\n"))
req_numbers = int(input("how many numbers do you like in your passwords?\n"))
req_symbols = int(input("How many symbols do you like in your password?\n"))

#Easy Level Password Generator
password = ""
for char in range(0, req_letters): 
    password += random.choice(letters)

for char in range(0, req_numbers): 
    password += random.choice(numbers)

for char in range(0, req_symbols):
    password += random.choice(symbols)

print(password)

#Hard Level Password Generator
password_list = []
for char in range(0, req_letters): 
    password_list += random.choice(letters)

for char in range(0, req_numbers): 
    password_list += random.choice(numbers)

for char in range(0, req_symbols):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")





    










