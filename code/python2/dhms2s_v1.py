# dhms2s: converts time in days, hours, minutes, and seconds into seconds
# Created on Tue May  7 11:54:08 2019
# CPSC 128 Example Code
# S. Bulut May 7, 2019

print "Enter your values now,"
days = input("Enter days: ")
hours = input("Enter hours: ")
minutes = input("Enter minutes: ")
seconds = input("Enter seconds: ")
tot_seconds = days*24*60*60 + hours*60*60 + minutes*60 + seconds
print "Total seconds is", tot_seconds
