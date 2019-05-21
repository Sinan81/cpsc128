import random
import time as tm

start = tm.time()

ROLLS = 10**6
# Initialize counters to 0.
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
sevens = 0
eights = 0
nines = 0
tens = 0
elevens = 0
twelves = 0
# Roll dice many times and record frequency of outcomes.
for roll in range(ROLLS):
    outcome = random.randint(1, 6) + random.randint(1, 6)
    if outcome == 2:
        twos = twos + 1
    elif outcome == 3:
        threes = threes + 1
    elif outcome == 4:
        fours = fours + 1
    elif outcome == 5:
        fives = fives + 1
    elif outcome == 6:
        sixes = sixes + 1
    elif outcome == 7:
        sevens = sevens + 1
    elif outcome == 8:
        eights = eights + 1
    elif outcome == 9:
        nines = nines + 1
    elif outcome == 10:
        tens = tens + 1
    elif outcome == 11:
        elevens = elevens + 1
    else:
        twelves = twelves + 1
        
# Display results.
print("  =====================")
print("  Outcome | Occurrences") 
print("  --------+------------") 
print("      2   |%8d" % (twos) ) 
print("      3   |%8d" % (threes))
print("      4   |%8d" % (fours)  )
print("      5   |%8d" % (fives)   )
print("      6   |%8d" % (sixes)   )
print("      7   |%8d" % (sevens)   )
print("      8   |%8d" % (eights)  )
print("      9   |%8d" % (nines)  )
print("     10   |%8d" % (tens)   )
print("     11   |%8d" % (elevens))
print("     12   |%8d" % (twelves) )
print("  ---------------------")

end = tm.time()
print("Calculation completed in ",end-start," seconds")  