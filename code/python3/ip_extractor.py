# ip_extractor.py
fname = input('What file do you want to scan? ')
ip = input('What IP address do you want to scan for? ')
print()
f = open(fname, 'r')
for line in f:
    if line.find(ip) != -1:
        print(line)
