# read_coords_v2.py
coords = []
fname = input('Name of file to read from? ')
f = open(fname, 'r')
for line in f:
    coords.append( list( map(int,line.split()) ) )
f.close()
print('coords =', coords)

