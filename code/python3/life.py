# life.py
universe = [ [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
           ]
import pickle

f = open( 'pickled_universe.pickle', 'wb')
pickle.dump(universe, f)
f.close()
f = open('pickled_universe.pickle', 'rb')
u = pickle.load(f)
f.close()
print(u)


###test human readable protocol 
#f = open( 'pickled_universe.txt', 'wb')
#pickle.dump(universe, f, protocol=0)
#f.close()


### test file size for a big system    
#size = 100000
#universe = random.sample(range(size),size)
#
#import pickle
#f = open( 'test.pickle', 'wb')
#pickle.dump(universe, f)
#f.close()
#
#with open( 'test.txt', 'w') as f:
#    f.write(str(universe))    