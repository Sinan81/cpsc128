# draw_a_square.py
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
    # draw top row of the square
    for i in range(size):
        print(c, end='')
    print()
    
#    # draw the middle rows of the square
    for i in range(size-2):
        print(c, end='')
        for j in range(size-2):
            print(' ',end='')
        print(c)

    # draw the bottom row of the square
    for i in range(size):
        print(c, end='')
    print
    