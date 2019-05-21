# allgirsl_while.py

# simulate 1000 4-child families
# count how many of them have all-daughters
import random

allgirls = 0
family=0
while family < 1000:

    daughters = 0
    birth = 0
    while birth < 4:
        # assign 0 -> a boy, 1-> a girl
        if random.randint(0,1) == 1:
            daughters = daughters + 1
        birth = birth + 1
        
    if daughters == 4:
        allgirls = allgirls + 1

    family = family + 1
        
print("Percentage of all girl families is: %1.2f" % (allgirls/1000.*100.) )
