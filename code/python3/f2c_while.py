# f2c_while.py: converts a given temperature in Fahrenheit to Celsius
# CPSC 128 Example program
# S. Bulut, Spring 2018-19 

print("This program converts temperatures from Fahrenheit to Celsius.")

again='y'
while again=='y' or again=='Y':
    
    print("Enter a temperature in Fahrenheit (e.g. 10) and press Enter.")
    temp_in_f = eval(input("Temperature in Fahrenheit: "))
    temp_in_c = (temp_in_f - 32)*5/9
    print(temp_in_f, "degrees Fahrenheit =", temp_in_c, "degrees Celsius.")
    
    again = input("Do it again (y/n)? ")
    
print("bye now")

