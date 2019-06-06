##shelve_example.py
import shelve
s = shelve.open('test_shelve')
s['bob'] = 42
s['liz']=[31]
s.close()

##alternative
#with shelve.open('test_shelve') as s:
#    s['bob'] = 42
#    s['liz']=[31]


s = shelve.open('test_shelve')
for key in s.keys():
    print(key, ':', s[key])
    
s['liz'][0] = 30
s['liz']