# dhms2s: converts time in days, hours, minutes, and seconds into seconds
# Created on Tue May  7 11:54:08 2019
# CPSC 128 Example Code
# S. Bulut May 7, 2019

print("Enter your values now,")

days = eval(input("Enter days: "))

hours = eval(input("Enter hours: "))

minutes = eval(input("Enter minutes: "))

seconds = eval(input("Enter seconds: "))

tot_seconds = ((days*24 + hours)*60 + minutes)*60 + seconds

print("Total seconds is", tot_seconds)
