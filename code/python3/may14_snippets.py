#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:35:12 2019

@author: sbulut
"""

value = eval(input("Enter an integer (e.g, 23 or -118): "))
if value < 0:
    print(value, "is negative")
else:
    print(value, " is positive")



value = eval(input( "Enter an integer (e.g. 23 or -118): " ))
if value < 0:
    print(value, "is negative")
else:
    if value == 0:
        print(value, "is neither positive nor negative")
    else:
        print(value, "is positive")
        

value = eval(input( "Enter an integer (e.g, 23 or -118): " ))
if value < 0:
  print(value, "is negative")
elif value == 0:
  print(value, "is neither positive nor negative")
else:
  print(value, "is positive")
  
    
value = eval(input( "Enter an integer (e.g. 23 or -118): " ))

if value < -100:
    print(value, "is very negative")
elif value < 0:
    print(value, "is negative")
elif value == 0:
    print(value, "is neither positive nor negative")
else:
    print(value, "is positive")
    
age >= 20 and age < 30


age >= 20 or income < 18.45    

# Version 1.
print " ... " # Instructions to user
grade = eval(input("..."))
if grade >= 95 and grade <= 100:
    print("A+")
if grade >= 86 and grade <= 94:
    print("A")
if grade >= 80 and grade <= 85:
    print("A-")
# ...
# and so on down to
# ...
if grade >= 50 and grade <= 54:
    print("D")
if grade >= 0 and grade <= 50:
    print("F")
if grade < 0 or grade > 100:
    print("Error: The grade must be between 0 and 100.")
    



# Version 2.
print(" ... ") # Instructions to user
grade = eval(input( " ... " ))
if grade >= 95 and grade <= 100:
    print("A+")
elif grade >= 86 and grade <= 94:
    print("A")
elif grade >= 80 and grade <= 85:
    print("A-")
# ...
# and so on down to
# ...
elif grade >= 50 and grade <= 54:
    print("D")
elif grade >= 0 and grade <= 50:
    print("F")
else:
    print("Error: The grade must be between 0 and 100.")
    
    
# Version 3.
print(" ... ") # Instructions to user
grade = eval(input("..."))
if grade > 100 or grade < 0:
    print("Error: The grade must be between 0 and 100.")
elif grade >= 95:
    print("A+")
elif grade >= 86:
    print("A")
elif grade >= 80:
    print("A-")
# ...
# and so on down to
# ...
elif grade >= 50:
    print("D")
elif grade >= 0:
    print("F")