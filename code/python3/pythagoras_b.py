# pythagoras_b.py
# S. Bulut  2019
# T. Topper 2015

print('''
===========================
Right-angle tirangle tester
---------------------------

Enter the lengths of the sides of your triangle and I will let you know
if it has a right angle or not
''')

a = eval(input("Length of the first side ="))
b = eval(input("Length of the second side ="))
c = eval(input("Length of the third side ="))

# find hypoteneuse
hypo = a
if b > hypo:
    hypo = b

if c > hypo:
    hypo = c

if a**2 + b**2 + c**2 == 2*hypo**2
    print("That is a right angled triangle")
else:
    print("That is NOT a right angled triangle.")