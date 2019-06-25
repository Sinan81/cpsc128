# find_average.py 
#   calculates average of inputted values
#   
# CPSC128 example code
# S. Bulut, May 2019

#example usage of sentinel number

print("This program calculates average of numbers entered by user.")
total = 0
count = 0
num = 0
while num != -1:
	num = eval(input("Enter the next number or enter -1 to calc average: "))
	if num != -1:
		total = total + num
		count = count +1

av = float(total)/float(count)

print("average is: ", av)
