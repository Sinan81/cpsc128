# s2dhms.py -- converts a time in seconds to
# its equivalent in days, hours, minutes and seconds.
#
# CPSC 128 Demonstration Program
#
# S. Bulut, Spring 2018-19

SECS_PER_DAY = 24 * 60 * 60
SECS_PER_HOUR = 60 * 60
SECS_PER_MINUTE = 60

# Input.
print("=====================================================")
print("     Seconds to Days, Hours, Minutes and Seconds")
print("-----------------------------------------------------")
print
print("This program converts a number of seconds to its")
print("equivalent in days, hours, minutes and seconds.")
tot_seconds = eval(input("Enter the number of seconds now (e.g. 116529): "))
print

# Processing.
days = tot_seconds // SECS_PER_DAY
remainder = tot_seconds % SECS_PER_DAY
hours = remainder // SECS_PER_HOUR
remainder = remainder % SECS_PER_HOUR
minutes = remainder // SECS_PER_MINUTE
remainder = remainder % SECS_PER_MINUTE

# Output.
print(tot_seconds, "seconds =", days, "days,", hours, "hours,",end="")
print(minutes, "minutes and", remainder, "seconds")
