# Assignment #5

This assignment is due June 17th Monday. Please make sure to follow [Python style guidelines](README.md#cpsc-128-python-style-guidelines). 

## Problem 1: Text file practice

**1-A** Write a module containing three functions. When run, the module should prompt the user for a filename and a number of lines (let's refer to it as n) and then call each function in turn with these parameters.

- The function `head` should return a list containing the first n lines of the file.

- The function `tail` should return a list containing the last n lines of the file.

- The function `longest` should return a list containing the longest n lines of the file.

The output of running the module might look like this:

```
Name of file to test with: pooh.txt
Number of lines to display: 3

head says the first 3 lines are:
The more it snows
  (Tiddely pom),
The more it goes

tail says the last 3 lines are:
 How cold my toes
  (Tiddely pom),
 Are growing.

longest says the longest 3 lines are:
The more it snows
The more it goes
And nobody knows
```

Since the file could be very long you will *not want to read the whole thing* into memory as a list of lines...

**1-B** `touch`

This is a simple exercise on writing to a file. Create a function called `touch(filename)` which accepts a filename as argument, and creates an empty file via writing an empty string to this file. The function should check if the file already exists (see below), and if so prompts the user that it can't create the empty file and quits

```python
# Example Check if a file exists in the current working director:
import os
os.path.exists("file.txt")
#get current working directory
os.getcwd()
```

Here is a sample run:
```
from touchexercise import touch

touch('hello2.txt')
creating empty file:  hello2.txt

touch('hello2.txt')
file already exists at the current working directory:
/home/sbulut/github/cpsc128/code/python3
quitting ...
```


## Problem 2: Every letter counts

Write a function `letter_frequency` that takes a string and returns a dictionary showing how often each letter of the alphabet occurs in the string. The dictionary should use the letters as keys and the letters' counts as values.

## Problem 3: Shelve practice

This is a simple exercise on working with `shelve` module. Complete the program `crud_controller.py` (located under assignment5 folder in the github repository), i.e. insert code for the remaining functions, and make sure adding new quotes can't delete existing ones. For simplicity, assume that there will be only one quote per author in the database. Remember to review class slides on shelves before attempting this problem.

Sample run
```

What file of quotes would you like to work with? quotes3

    Actions
    -------
    c - create a quote to add to the collection
    r - retrieve a quote from the collection and display it
    u - update a quote in the collection
    d - delete a quote from the collection
    l - list all the items in the collection
    q - exit

    Your choice?

c

Who is the author of the quote? Albert Einstein

What did they say or write? God does not play dice.

    Actions
    -------
    ...
    Your choice?

l
Here are the contents of the shelve quotes3 :
Einstein : ['Albert Einstein', 'God does not play dice.']

    Actions
    -------
    ...
    Your choice?

c

Who is the author of the quote? Albert Einstein
Entry for this author already exists

    Actions
    -------
	...
    Your choice?

r

Enter lastname of the author:
Einstein
Quote is:  "God does not play dice."

    Actions
    -------
    ...
    Your choice?
q
```
## Problem 4: Plotting & timing

This question about timing code and plotting results. We will take this opportunity the highlight the efficiency difference between a list and a dictionary when searching for entries. Write a program that does the following:
```
for nlines in [10,100,1000,10**4, 10**5]
    read nlines from words.txt into a list
    pick a random item from the list
    do a look up operation using "in" operator (item in list)
    measure and record look-up time
    append the result to a list (say lookuptime_list)

    read nlines from words.txt into a dictionary
    using the above picked random item, do a look up operation using "in" operator (item in dict)
    measure and record look-up time
    append the result to a list (say lookuptime_dict)

plot the results on the same graph: 
    nlist vs lookuptime_list, and nlist vs lookuptime_dict
```
"words.txt" is located under assignment5 folder in the github repository. You will need to check out parts of Python cheats on timing and plotting.












