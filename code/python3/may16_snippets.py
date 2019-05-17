# example: five hi
counter = 5
while counter >0:
    print("Hi!")
    counter=counter-1
    
# example: five hi
counter = 5
while counter >0:
    print("Hi!")
    counter -= 1
    
# infinite loop
while True:
    print("Help! I'm stuck in a loop!")


validgrade = False #initialize
while not validgrade:
    print("please enter a valid grade between 0 and 100")
    grade = eval(input("Enter grade"))
    validgrade = grade >= 0 and grade <=100
    

# input validation v2
while True:
    print("please enter a valid grade between 0 and 100")
    grade = eval(input("Enter grade\n"))
    validgrade = grade >= 0 and grade <=100
    if validgrade:
        break
    
# repeat a program
# here is a structure to enable user run a code again
# without having to restart the program
again='y'
while again=='y' or again=='Y':
    
    #
    # put the code you want to repeat here
    #
    
    again = input("Do it again (y/n)? ")
    
print("bye now")

# playing computer v1
x = 0
while x < 5:
    y = 0
    while y < 3:
        print("*")
        y=y+1
    print()
    x = x+1
    
    
# playing computer v2
x = 0
while x < 5:
    y = 0
    while y < x:
        print("*")
        y=y+1
    print()
    x = x+1
    
# nested while
while test1:
    [statement]
    while test2:
        statement
        
# for loop examples
for c in 'This is a vertical text!':
    print(c)

for x in [1, 2, 3]:
    print(x)

for x in range(3):
    print(x)
    
    
# five hi! for loop
for x in [1, 2, 3, 4, 5]:
    print("Hi!")

print('Done!')



















