# write_coords2.py
coords = [[12, 31], [75, 19], [28, 51]]
fname = input('Name of file to create? ')
f = open(fname, 'w')
f.write(str(coords))
f.close()