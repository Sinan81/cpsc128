# gazinta.py -- this code takes in two numbers, and determines if the second
#   one divides the first one exactly.
# S. Bulut May 2019

print("""Wondering if one number "goes into" another?
Give me the numbers (big one first) and I'll tell you.""")

a = eval(input("First number = "))

b = eval(input("Second number ="))

if b == 0:
    print("Sorry division by 0 is undefined!")
elif a%b == 0:
    print(b," does go into", a, "exactly")
else:
    print(b," does NOT go into", a, "exactly")