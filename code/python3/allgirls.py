# allgirsl_while.py

# simulate 1000 4-child families
# count how many of them have all-daughters
import random

allgirls = 0
for family in range(1000):

    daughters = 0
    for birth in range(4):
        # assign 0 -> a boy, 1-> a girl
        if random.randint(0,1) == 1:
            daughters = daughters + 1

    if daughters == 4:
        allgirls = allgirls + 1

        
print("Percentage of all girl families is: %1.2f" % (allgirls/1000.*100) )
