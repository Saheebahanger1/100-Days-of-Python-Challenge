# Subscripting from first to last [0 - ...]
print("Hello"[0]) # the result will be 'H'.

# Subscripting from last to first[-1 to ...]
print("Hello"[-5]) # the result will be 'H'.

# 2:Integers
print(10 + 20) # the result will be 30

# 3: Float = include decimal values (eg=24.15)
print(3.142) #output=is 3.142

# 4: Boolean = (true/false)
print(True) #True
print(False) #False

# checking data type
print(type("Saheeb")) #String
print(type(1234)) #Integer
print(type(3.14)) #Float
print(type(True)) #Boolean

#Type Coversion
print("123" + "456") # Result = 123456
print(int("123") + int("456")) # Result = 579(sum)

# Correct the piece of code
#print("Number of letters in your name: " + len(input("Enter your name: ")))

name_of_the_user = input("Enter your name: ") #Enter your name: Saheeb.
length_of_name = len(name_of_the_user) #calculate the letters.
print("Number of letters in your name: " + str(length_of_name)) #Number of letters in your name: 6.

# Mathematical operations 
print(1 + 2) # Addition , result=3
print( 2- 1) # Subtraction , result=1
print(2*3) # Multiplication , result=6 , {Asterisk(*)}
print(4/2) # Division with Decimal , result=2.0 ("/" = remainder ,"%" = remainder )
print(6//2) #Division W/O Decimal , result=2
print(2**2) #Exponents , result 2 raised power 2 = 4.

# PEMDAS 1.Parantheses 2.Exponents 3.Multiply 4.Divide 5.Add 6.Subtract
# NOTE : Calculation happens from Left-Right.(Eg = 3*3+3/3-3)
print(3 * 3 + 3 / 3 - 3) # result = 7 (as per PEMDAS Rule)
#->step 1 = 3*3=9
#->step 2 = 3/3=1
#->step 3 = 9+1=10
#->step 4 = 10 - 3 =(7 ans)

# Rounding Off
print(round(3.9)) # Decimal No < 5 = Int of that no. , Decimal No > 5 = Int which is after that no. 
print (round(3.96825 , 3)) # Results 3.968 , 3 indicates No. after decimal.

# F-string = consists of all data types.
# syntax = print(f "my age is { ! } years.)
age=input("Enter your Age: ") # Enter Your Age: _19
print(f"I am {age} years old.") # Results= I am 19 years old.


# Day-2 Project : Tip Calculator.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? Rs: "))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill? "))
Total_bill_with_tip = bill * (1 + tip / 100)
print(Total_bill_with_tip)
bill_per_person = Total_bill_with_tip / people
Final_amount = round(bill_per_person , 2)
print(f"Each Person should pay : {Final_amount}")

# ------DAY-2 COMPLETED------