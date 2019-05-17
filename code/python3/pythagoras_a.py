# pythagoras.py
# S. Bulut  2019
# T. Topper 2015

print('''
===========================
Right-angle tirangle tester
---------------------------

Enter the lengths of the sides of your \triangle and I will let you know
if it has a right angle or not
''')

a = eval(input("Length of the first side ="))
b = eval(input("Length of the second side ="))
c = eval(input("Length of the third side ="))

print("hello\
world")

if a**2 + b**2 == c**2 or \
    a**2 + c**2 == b**2 or\
    b**2 + c**2 == a**2:
    print("That is a right angled triangle")
else:
    print("That is NOT a right angled triangle.")