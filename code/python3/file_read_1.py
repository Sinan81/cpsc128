# file_read_1.py
f = open('text_file.txt', 'r') # Open the file.
for line in f:                 # Iterate through the file a line at a time.
    print(line, end='')        # Process the current line.
f.close()                      # Close the file.


# alternative with 'with'
with open('text_file.txt', 'r') as f:
    for line in f:                 
        print(line, end='')
