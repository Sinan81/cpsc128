# f2c.py: converts a given temperature in Fahrenheit to Celsius
# CPSC 128 Example program
# S. Bulut, Spring 2018-19 

print("This program converts temperatures from Fahrenheit to Celsius.")

print("Enter a temperature in Fahrenheit (e.g. 10) and press Enter.")

temp_in_f = eval(input("Temperature in Fahrenheit: "))

#https://en.wikipedia.org/wiki/Fahrenheit
temp_in_c = (temp_in_f - 32)*5/9

print(temp_in_f, "degrees Fahrenheit =", temp_in_c, "degrees Celsius.")
