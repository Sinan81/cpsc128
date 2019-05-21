# draw_a_square_v2.py
# Draw a hallow square on screen. The size and character to use are chosen
# by the user.
#
# CPSC 128 example code
# S. Bulut
# May 2019

print("This program will draw a hallow square on the screen")
print()

size = eval(input("How large a square would you like?"))
c = input("Which character should I use to draw it?")

if size < 1:
    print("Sorry, can't handle negative sizes or null size.")
elif size == 1:
    print('c')
else:
    for row in range(size):
        for col in range(size):
            if row==0 or row==size-1 or col==0 or col==size-1:
                print(c, end='')
            else:
                print(' ', end='')
        print()