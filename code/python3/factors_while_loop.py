# factors_v1.py
# calculate all factors of a given number
#
# CPSC128 example code
# S. Bulut, May 2019

print("This program will display all factors of the number you enter")
num = eval(input("Enter an integer number"))
print()

print("%d's factors are:" % num)
# alternative print statement with sep='' trick
# print(num,"'s factors are:", sep='')
divisor=1
while divisor <= num:
    if num%divisor == 0:
        print(divisor, num/divisor)
    divisor=divisor+1
