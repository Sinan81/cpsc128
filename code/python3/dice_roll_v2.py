import random
import time as tm
start = tm.time()

ROLLS = 10**6

# Initialize counters to 0.
counters = [0] * 11

# Roll dice many times and record frequency of outcomes.
for roll in range(ROLLS):
    outcome = random.randint(1, 6) + random.randint(1, 6)
    # Now increment the appropriate counter.
    # Notice that no testing is needed because we can calculate the index of the matching entry.
    counters[outcome-2] = counters[outcome-2] + 1
        
# Display results.
print("  =====================")  
print("  Outcome | Occurrences")  
print("  --------+------------")  
for posn in range(11):
    print("%7d   |%8d" % (posn+2, counters[posn]))
print("  ---------------------")

end = tm.time()
print("Calculation completed in ",end-start," seconds")