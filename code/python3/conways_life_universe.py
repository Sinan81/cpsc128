universe = [ [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
           ]

for row in universe:
    for item in row:
        print(item, end='')
    print()

print(8*'_')
for row in universe:
    for item in row:
        if item == 0:
            c = ' '
        else:
            c = '*'
        print(c, end='')
    print('|')
print(8*'_'+'|')
    