
# loop to get multiple inputs from user
n = 0
again = 'y'
nsum = 0
while again == 'y' or again == 'Y':
    # get nth number
    nth_number=eval(input("Enter the next number!"))
    # ask user if they want to continue entering numbers
    again = input("Do you want to continue entering numbers? (y/n)")
    #keep track of total number of inputs
    n = n + 1
    #save all entered numbers to nlist
    nsum = nsum + nth_number
 
# calc average: nsum/N
average = nsum/n
print(average)

# loop to get multiple inputs from user v2
N = eval(input("How many numbers will you enter in total for this calculation?\n"))
n = 1
again = 'y'
nsum = 0
while n <= N:
    # get nth number
    nth_number=eval(input("Enter the next number!"))
    # ask user if they want to continue entering numbers
#    again = input("Do you want to continue entering numbers? (y/n)")
    #keep track of total number of inputs
    n = n + 1
    print("iteration number",n)
    #save all entered numbers to nlist
    nsum = nsum + nth_number
 
# calc average: nsum/N
average = nsum/n
print(average)


# loop to get multiple inputs from user v2
sentinel = eval(input("Enter a sentinel value (something other than -1) to be used to break the loop \n"))
n = 0
again = 'y'
nsum = 0
nth_number = -1
while nth_number != sentinel:
    # get nth number
    nth_number=eval(input("Enter the next number!"))
    # ask user if they want to continue entering numbers
#    again = input("Do you want to continue entering numbers? (y/n)")
    #keep track of total number of inputs
    n = n + 1
    print("iteration number",n)
    #save all entered numbers to nlist
    if nth_number != sentinel:
        nsum = nsum + nth_number
 
# calc average: nsum/N
average = nsum/n
print(average)