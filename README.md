# CPSC128
This is a repository for the CPSCS 128 "Introduction to Programming using Python" course.

See the syllabus: [CPSC 128 Spring 2018-19 Syllabus](files/CPSC_128_outline_2019.pdf)

## Table of Contents

* [Announcements](#announcements)
* [Assignments](#assignments)
* [Remarks on the Final Exam](#remarks-on-the-final-exam)
* [Slides](#slides)
* [Lecture Notes](#lecture-notes)
* [Python Resources](#online-python-resources)
* [Outline](#outline)
* [git cheats](#git-cheatsheet)
* [Python cheats](#python-cheatsheet)
* [Pythonic details](#pythonic-details)
* [CPSC 128 Python Style Guidelines](#cpsc-128-python-style-guidelines)
* [computing setup](#computing-setup)
* [github markdown](#github-markdown)
* [vim cheats](#vim-cheats)

## Announcements

Please make sure to subscribe to 'Announcements' issue so that you get notified. 

[https://github.com/Sinan81/cpsc128/issues/4]

* Jun 27, Thu, Assignment-5's are marked.
* Jun 26, Wed, Final exams are marked
* Jun 22, Sat, the section 'Remarks on the final exam' is posted.
* Jun 22, Sat, Slides for the entire course are posted.
* Jun 20, Thu, Slides for June 20 "class is posted.
* Jun 19, Wed, Assignment #4 is marked.
* Jun 18, Tue, Slides for June 18th class posted
* Jun 17, Mon, Assignment #6 is posted.
* Jun 17, Mon, Slides for Jun-13th class is posted.
* Jun 12, Wed, Assignment #3 is marked.
* Jun 11, Tue, Slides for Jun-11th class is posted.
* Jun 10, Mon, Assignment 5 is posted.
* Jun 06, Wed, Slides for Jun-6th class is posted.
* Jun 05, Wed, Slides for Jun-4th class is posted.
* Jun 05, Wed, Assignment #2 is marked.
* Jun 03, Mon, Assignment #4 is posted.
* Jun 02, Sat, May 30 class slides posted
* Jun 01, Sat, May 28 class slides posted
* May 29, Wed, More lecture notes are posted
* May 25, Sat, Assignment #3 is posted.
* May 24, Fri, Slides for May 21 and 23 classes are posted.
* May 23, Thu, Assignment1's are marked.
* May 18, Sat, python cheatsheet is improved (see below)
* May 17, Fri, Assignment #2 is posted.

## Lecture Notes (by Tim Topper)
In this course, to a significant extent I will be following previous instructor's (Tim Topper) contents. Accordingly, you might find his lecture notes useful:

[Lecture Notes](files/lecture_notes_cpsc128/)

After cloning this repository to your computer open the following file on an internet browser: `files/lecture_notes_cpsc128/index.html`

## Assignments

[Assignment 1](assignment1.md) Due May 20, Monday

[Assignment 2](assignment2.ipynb) Due May 24, Friday

[Assignment 3](assignment3.md) Due Jun 3rd, Monday

[Assignment 4](assignment4.md) Due Jun 10, Monday

[Assignment 5](assignment5.md) Due Jun 17, Monday

[Assignment 6](assignment6.md) Due Jun 24, Monday

## Remarks on the Final Exam

Please see the [Sample Final Exam](files/sample_final_exam.pdf). The solution to most of the problems can be found in course slides. For others, I will try to post solutions soon. The format of the final example will be similar. In preparing for the final exam, you might want to check out the following list of 'examinable topics'. 

### Examinable Topics

We will attempt to cover all the following topics on the final exam, though not all topics will be given equal weight. For example, the single most important skill is the ability to devise solution procedures for problems in terms of sequence, selection (if) and iteration (for and while).

* Base skill: IPO programming: Using Python to calculate values of formulas, e.g. wind-chill, unit conversions.
* Core skill: Combining if, while, for to express algorithmic procedures.
* Technique: Pulling apart numbers using % and /.
* Technique: Knowing when to use input and when to use eval(input()).
* Technique: Input validation using while.
* Technique: Using counters in programs.
* Technique: Using flag variables, i.e. Boolean variables that record state, e.g. `while not game_over:`, `while not done:`, `if game_lost:`.
* Core skill: Defining functions. Knowing how to do it, and knowing when to do it.
* Approach: Using randomness to simulate events, e.g. four daughters
* Data representation: Representing things using lists, e.g. playing cards.
* Data representation: Creating and interpreting heterogeneous data structures (lists of lists, lists of dictionaries, dictionaries of lists, etc.), e.g. the cave system for Hunt the Wumpus.
* Technique: Processing strings using string operations, as in the password checking program.
* Technique: Processing lists, e.g. CD shuffle, `is_straight()`.
* Technique: Using vs changing lists, i.e. how to change a list in place, and how to avoid changing a list.
* Technique: Converting lists to strings and vice versa.
* Data representation: Using and processing dictionaries, e.g. for counting.
* Data representation: File processing, e.g. the temperature data file.
* Approach: Parameterizing code for generality. (And on a minor note, using 'symbolic constants').
* OOD: object types → classes → attributes & methods (tell, ask)
* OOP concepts: Abstraction, Inheritance, Polymorphism.
* OOP: Defining (base) classes, reverse engineering them when necessary.
* OOP: Modifying a class via inheritance. Using inheritance to avoid code duplication.
* Problem domains: Playing cards, Hunt the Wumpus
* Software development:
1. By hand → Pseudocode → Python
2. Documentation
3. Divide and conquer
4. Design first; code second
5. Incremental development


## Outline

0. Course start-up.
* Part I: Procedural programming
1. Introduction to computer science.
2. SIPO (sequence, input, processing and output) programming.
3. Selection control structures.
4. Repetition control structures.
* Part II: Object-based programming
5. Aggregate data types 1: Lists and strings.
6. Functions.
7. Aggregate data types 2: Dictionaries.
8. Text files.
* Part III: Object-oriented programming
9. Object-oriented programming (OOP) 1: Encapsulation.
10. Object-oriented design (OOD).
11. Object-oriented programming (OOP) 2: Polymorphism and inheritance.
12. TBA
* Final Examination

## Online Python Resources
You might want to check out the following online resources:

* [Official Python Tutorial](https://docs.python.org/3.6/tutorial/)
* [Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/thinkpython/html/index.html)
* [Learn Python The Hard Way](https://learnpythonthehardway.org/book/index.html)
* [Hand-On Python: A Tutorial Introduction for Beginners](http://anh.cs.luc.edu//python/hands-on/handsonHtml/handson.html)

## Slides

The slides for the entire course can be found at: [CPSC128 all slides](files/cpsc128_slides_complete.pdf)

|	Tues	 | Thurs |
|--------------------------------------- | --------------------------------------- |
|                                        | [May  2 Computing Setup & Intro](files/cpsc128_slides_may2.pdf)  | 
| [May  7 Intro & SIPO ](files/cpsc128_slides_may7.pdf) | [May  9 SIPO](files/cpsc128_slides_may9.pdf) |
| [May 14 Selection with If](files/cpsc128_slides_may14.pdf) | [May 16 Repetition](files/cpsc128_slides_may16.pdf) |
| [May 21 for loop & Lists](files/cpsc128_slides_may21.pdf) | [May 23 Lists](files/cpsc128_slides_may23.pdf) |
| [May 28 Lists & Strings](files/cpsc128_slides_may28.pdf) | [May 30 Functions, Modules](files/cpsc128_slides_may30.pdf) |
| [Jun 04 Dictionaries](files/cpsc128_slides_jun04.pdf) |  [Jun 06 Persistence: writing to files](files/cpsc128_slides_jun06.pdf)|
| [Jun 11 Object Oriented Programming](files/cpsc128_slides_jun11.pdf) |  [Jun 13 Object Oriented Design](files/cpsc128_slides_jun13.pdf) |
| [Jun 18 Inheritence & Polymorphism](files/cpsc128_slides_jun18.pdf) | [Jun 20 Wrap up & Remarks & Sample Final Exam](files/cpsc128_slides_jun20.pdf)| 

## git cheatsheet

If created new file, first tell `git` to track it
```
git add mycode.py
```

If a new file added or a current file is modified, save it via
```
git commit -m 'commit message' mycode.py
```

Push modifications in local repo to the remote git server (github)
```
git push
```

To download github repository:

```
git clone https://github.com/Sinan81/cpsc128.git
```

Already downloaded a repo, but want to pull updates to it?. First navigate to the repository folder on git-bash console and do a pull:
```
cd ~/cpsc128
git pull
```

## python cheatsheet

- get help via `help()`

- get input from user
```python
# get integer, float, .. input
inval = eval(input("Enter an integer")) 
# string input
inval = input("Enter a string input")
```
- divison (Python3)
```python
#integer division: yields integer, discards decimal places
9//5

#float division
9/5
```

- print statement
```python
# syntax print a list of stuff separated by ', '
print(list)

# example
s='world'
print("hello ", s, '!', 5+7)

#hold the current output line open (as opposed to going to the next line)
print("Hello", end='')
```
- import a module/library and use a method from this module:

```python
import math
math.sqrt(9)

import math as m
m.sqrt(9)

from math import sqrt
sqrt(9)

from math import *
sqrt(9)
```
- selection using if
```python
# example 1
if x < 0:
    print("x is negative")

# example 2
if flip == 1:
    print("Head")
else:
    print("Tail")

# example 3
if num < 0:
    print("num is negative")
elif num == 0:
    print("num is zero")
else:
    print("num is positive")
```
- relational & logical operators

| operator | explanation |
| --- | --- |
| < | less than |
| <= | less than or equal to |
| == | equal to |
| != | not equal to |  
| >= | greater than or equal to |
| >  | greater than |
| a and b | `True` if both a & b are true |
| a or b  | `True` if either a or b are True |
| not a   | negation operator: e.q. **not** True -> False |

- use `random` module to generate random numbers
```python
from random import randomint random
randomint(1,100) # generates a random integer between 1 and 100
random() # generates a random float betwee 0. and 1.0 inclusive
```
- repetition with `while`
```python
# syntax is
while test:
    statement
```
Basic usage
```python
x=1 #initialize
while x < 1:
    print(x)
    x = x+1
```
Input validation
```python
num = input( "Enter a number between 1 and 100: " )
while num < 1 or num > 100:
    print("Oops, your input value (", num, ") is out of range.")
    num = input( "Be sure to enter a value between 1 and 100: " )
```
Repeating a program
```python
again = "y"
while again == "y" or again == "Y" or again == "yes" or again == "Yes":
    #
    # Put the body of your program here
    #
    again = input( "Play again (y/n)? " )
print("Thanks for playing")
```
- modularity: functions & modules

```python
#define a function

def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

# a function can be in a return statement
def is_odd(x):
    return not is_even(x)
```

A module is a python program. Make sure to put extra stuff such as print statements 
after `if __name__ ...` section so that print statments aren't spamming 
the `stdout` or we're not wasting computational time on running extra stuff when the 
module is imported by a python program.  

A module is documented using docstrings which are accessed via `help()`. 

```python
# mynumbers.py
'''This module includes numbers related methods, attributes, etc.
Just a simple example of a module
'''

def is_even(x):
    '''Check if a given number is even.
    Returns a Boolean value.'''
    return x%2 == 0

def is_odd(x):
    '''Check if a given number is odd.
    Returns a Boolean value.'''
    return not is_even(x)

# extra stuff, won't run if imported by another program
if __name__ == '__main__':
    x = 13
    print( is_even(x), is_odd(x))
```
Accessing help for module and functions:
```python
help(mynumbers)
help(mynumbers.is_even)
```

Named and optional parameters:
```python
#inputs with default values like `b=0` are optional:
def fpoly(x,a,b=0,c=0)
    return a*x**2 + b*x + c

#note below how Python is not complaining that
#   we didn't provide b,c
In [1]: fpoly(2,1)
Out[1]: 4

#'named parameter' trick enables us to enter input values out of order
In [72]: fpoly(c=1,b=1,a=0,x=2)
Out[72]: 3

In [72]: fpoly(a=1,x=2)
Out[72]: 4
```

- working with lists

See `help(list)` or `dir(list)` for all list atrributes and methods.

```python
#create list
l = list(range(10))               
l = [19, 'a', 3.14, 'Tea']

#check if an item exists in l using **in** construct 
19 in l                   

#iterate over list items
for item in l:
    print(item)

#access individual items in a list 
l[0]                       #0th item
l[1]                       #1st item                        
l[-1]                      #the last item
l[1:4]                     #get a slice of list (items 1,2, and 3) 

len(l)                     #number of items in list 
del(l[2])                  #delete item by index 
l = l + ['bye']       #concatenate two lists 
2*l                        #concatenate l twice.   

l.append(2)                #append item to the list 
l.insert(1,'hi')           #insert 'hi' before index 1  
l.remove('a')              #delete item by value 
l.pop()                    #delete the last item in the list 
l.index('Tea')             #returns position of item 'Tea' 
l.count('bye')             #counts number of 'bye's in the list 
l.sort()                   #sort the list 
l.reverse()                #reverse the order of the list 
l.extend()                 #extend list by appending items from an **iterable**
```

- working with strings

See `help(str)` or `dir(str)` for all str atrributes and methods.

```python

s = 'Hello World'               #create string
s = ''.join(alist)              #create string from a list

#iterate over characters in a string
for c in s:
    print(c)

# access
s[0]                            #get 0th element
s[1]                            #get 1st element
s[-1]                           #get the last element
s[1:4]                          #get a slice of string (characters 1,2, and 3)

# add
s = s + 'a word'                #concatenate
2*s                             #concatenate s twice. 

# info about a string
len(s)                          #returns the length of string
s.find('Tea')                   #returns position where first occurance of 'Tea' begins
s.count('o')                    #counts number of 'o's in the string
'l' in s                        #test if a substring is contained in a longer string

# misc. str methods
s[2].isalpha()                  #check if s[2] is alphabetical, i.e A-Z
'867-395-0892'.split('-')       #split the string into words assuming '-' is the seperator (delimeter)  
s.lower()                       #convert to lowercase
s[1].isupper()                  #check if s[1] is uppercase
```
- working with dictionaries

```python
# working with dictionary type
len(d)      # returns number of items in d
d.keys()    # returns a view of keys in d
d.values()  # returns a view of values in d
k in d      # returns True if k in d 
d[k]        # returns value associated with key k   
d[k] = v    # associates value v with key k
del d[k]    # removes entry with key k from d
d.pop(k)    # remove entry with key k but get value
for k in d: # iterate over keys in d
```

persistence

```python
#openfile in read mode (hence 'r')
f = open('filename.txt', 'r') #get file object
for line in f: #default iteration method is line by line
    print(line)
f.close() #make sure the close the file once done with it

#a newer method of dealing with files
#which doesn't require a f.close() step
with open('filename.txt', 'r' as f:
    for line in f:
        print(line)

#read entire file to as string
f = open('filename.txt', 'r') #get file object
s = f.read()
print(s)
f.close() #make sure the close the file once done with it

#read the entire file into a list of strings
#where each item is a line in the file
f = open('filename.txt', 'r') #get file object
lines = f.readlines()
print(lines)
f.close() #make sure the close the file once done with it

#search for a string in a file using 'find()' method for strings
#openfile in read mode (hence 'r')
f = open('filename.txt', 'r') #get file object
pattern='Hello'
for line in f: #default iteration method is line by line
    if line.find(pattern):
        print("pattern found in line: ", line)
f.close() #make sure the close the file once done with it

#writing to files (hence the 'w' mode)
f = open('filename.txt', 'w') #get file object
f.write("Hello\n")
f.close() #make sure the close the file once done with it

#appending to files (hence the 'a' mode)
f = open('filename.txt', 'a') #get file object
f.write("World\n")
f.close() #make sure the close the file once done with it
```

Saving/writing Python objects (lists etc) to disk

```python
# except for dictionaries, we should use pickling to save Python objects
import pickle
l = [0, 1, 2, 87, 202]
f.open('pickled_list.pickle', 'wb')
pickle.dump(l, f)
f.close()

#retreive a python object from disk
f.open('pickled_list.pickle', 'rb')
l = pickle.load(f)
f.close()
```

Shelves: the proper way to save dictionaries to disk

```python
#save dictionary to disk as shelve
import shelve
s = shelve.open('test_shelve')
s['bob'] = 42
s['liz'] = [31]
s.close()

#retrieve the dictionary from disk
s = shelve.open('test_shelve')
for key in s.keys():
    print(key, ':', s[key])

#mutable objects save in a dictionary can lead to subtle problems
#so update mutable values in shelves using a temporary variable
#make sure to open shelve with 'writeback=True' option
s = shelve.open('test_shelve', writeback=True)
tmp = s['liz'] #retreive a list
tmp[0] = 2  #update an item in list
s['liz'] = tmp
s.close()
```

Object oriented programming: Encapsulation (defining classes)

```python
# the syntax
class ClassName:
    def __init__(self, ...):
        ...
        
    def method1(self, ...):
        ...
    def method2(self, ...):
        ...

# example: die class
# die_class_0.py
import random

class Die:
    def __init__(self, n):
        self.nsides = n
        
    def roll(self):
        spots = random.randint(1,self.nsides)
        return spots

if __name__ == '__main__':
    d1 = Die(6)
    red = Die(20)
    
    print('Rolling d1 ...', end='')
    result = d1.roll()
    print('result =', result)
    
    print('Rolling red and d1 together gets you:', d1.roll() + red.roll() )
    print('The die d1 has %d sides' % (d1.nsides) )

```
OOP: Inheritence

```python
# Deck is a subclass or descendant of CardCollection
# In this simple example, Deck ony inherits the methods from CardCollection
#	as opposed to attributes as well.
class Deck(CardCollection):
    # Override ancestor's constructor, i.e. replace the default.
    def __init__(self):
        self.cards = []
        for cardnum in range(52):
            self.add( Card(cardnum) )
 
    # Alias the inherited method "size" as "cards_left",
    # because we usually ask how many cards are left in a
    # deck rather than asking about its size.
    def cards_left(self):
        return self.size()
 
    # Another alias. When using a deck of cards we talk about "dealing"
    # cards not "removing" them from the deck.
    def deal(self):
        return self.remove()

    # Add a new method, shuffle, that does not exist in ancestor class.
    def shuffle(self):
        ncards = len(self.cards)
        for swaps in reversed(range(ncards)):
            posn1 = random.randint(0, swaps)
            self.cards[posn1], self.cards[swaps] = self.cards[swaps], self.cards[posn1]

```

OOP: Polymorphism

```python
class Fraction:
    def __init__(self, n, d = 1):
        self.num = n # numerator
        self.den = d # denominator
        
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            bottom = self.den * other.den
            top = (self.num * other.den) + (other.num * self.den)
            return Fraction(top, bottom)
        elif isinstance(other, int):
            other = Fraction(other)
            bottom = self.den * other.den
            top = (self.num * other.den) + (other.num * self.den)
            return Fraction(top, bottom)
        
    def __le__(self, other):
        return self.num*other.den <= other.den*self.num
    
    def __getitem__(self, key):
        if key == 0:
            return self.num
        elif key == 1:
            return self.den
        
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            bottom = self.den * other.den
            top = (self.num * other.den) - (other.num * self.den)
            return Fraction(top, bottom)
        
if __name__ == '__main__':
    d1 = Fraction(2, 5)
    print(d1, '(s/b 2/5)')
    d2 = Fraction(4)
    print(d2, '(s/b 4/1)')
    d3 = d1 + d2
    print(d3, '(s/b 22/5)')
    if d1 <= d2:
        print(d1, 'is less than or equal', d2)
    else:
        print(d2, 'is greater than', d1)
    print(d1[0], d1[1], '(s/b 2 5)')
    print(d1 + 2, '(s/b 12/5)')
    print(d1 - 2, '(s/b -8/5)')
```

- basic plotting

A simple example where data is entered by hand: x=[1,2,3,4], y=[1,4,9,16].
```python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], label='data by hand')
plt.ylabel('axis label with equation $y=x^2$')
plt.xlabel('x')
plt.legend()
plt.show()
```
![plot example1](files/simple_plot_example_1.png)

Plotting a function
```python
import numpy as np
import matplotlib.pyplot as plt

#generate a list of x values to be fed to a function
#[1., 1.5, 2, 2.5 ...]
N = np.arange(1,20,0.5) 

plt.plot(N, N, label='linear search: $f(N)=N$')
plt.plot(N, np.log2(N), label='bisection method: $f(N)=log_2N$')

plt.ylabel('computation time')
plt.xlabel('problem size: N')
plt.legend()
plt.show()
```
yielding

![plot example2](files/simple_plot_example_2.png)

- timing code

```python
import time as tm
begin = tm.time()

#
# block of code to be timed
#

end = tm.time()
print('That took', end-begin, 'seconds')
```
- Python-3 vs Python-2

| code		| Python3			| Python2			|
----------- | ----------------- | ----------------- |
| `9/5`		| float division	| integer division	|
| `9//5`	| integer division	| float division	|
| `range(10)` | yields a range object do `list(range(10))` to obtain a list	|	yields a list	|
| `input()`	| raw input: input is captured as string | smart input, like `eval(input())` in Python3 |
| `print("Hello")` | print				| -	|
| `print "Hello"`	| -			| print	|

## Pythonic Details
Here I will be providing some interesting Python tricks. 
You are not expect to know these however you should be aware.
Since they don't belong a general introductory programming course, we're leaving them out.

```python
#List comprehenseion example: square of even numbers
[x**2 for x in range(10) if x%2 == 0]

#getting key,value pairs simultaneously from a dictionary
for k,v in d.items():
	print(k,v)

#map function: apply a given function to a list
In [35]: def f(x):
    ...:     return x**2
    ...: 

In [37]: list(map(f,range(5)))
Out[37]: [0, 1, 4, 9, 16]

#underscore as dummy loop variable
#generate n random integers between 0 and 99
#note in this case we don't need a loop variable
for _ in range(n):
	random.randint(100)

```

Exception handling usign `try...except` construct:

Python enables us to anticipate runtime errors and handle them gracefully.

```python
# it is possible that a file the program wants to read doesn't exist
# so handle this exception as follows.
try:
    with open('hellox.txt','r') as f:
        for line in f:
            print(line)

except FileNotFoundError:
    print("Caught it!")
```
More details can be found at [Python Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html).

## CPSC 128 Python Style Guidelines

These are extracted from the [official Python guidelines](https://www.python.org/dev/peps/pep-0008/) , so you will not have to wade through too many language features you won't recognize.

- Use four spaces for indentation. (IDLE does this for you. If you're using another editor, set it to use four space characters, not a tab character).
- Limit lines to 80 characters.
- Separate logical sections of a program with single blank lines.
- Begin every program with an opening comment block containing at least:

    \# filename
    
    \# Author
    
    \# Date
    
- Place `import` statements right after the opening comment block.
- Initialize variables as near their first use as possible.
- Do not leave a space between input and its opening (.
- Do not leave a space after ( or before ).
- Place a single space on each side of the binary operators: `=, ==, <, <=, !=, <>, >=, >, and, or, not, in` . Use spaces around arithmetic operators too, though in long expressions using grouping for readability takes precedence.
- Comments should be complete sentences.
- Comments should add to the code not repeat it, and should never state the obvious.
- Variable names should be lower_case.
- Constant names should be UPPER_CASE.


## github Markdown

If you want to create nice looking pages on github (such as README.md), you might want to checkout the following links for examples of Markdown (.md) language:

* https://guides.github.com/features/mastering-markdown/
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

## vim cheats

* hit 'i' to edit
* hit 'Esc' to escape edit mode
* do `:w` to save
* do `:q` to quit
* do `:wq` to save and quit
* hit '/' to do a search, and 'Esc' to get back to normal mode
* do 'p' to paste before, 'P' to paste after
* hit 'v' to switch to visual mode to select stuff for cutting, copying etc.

## Computing Setup

* python3
* git: version control
* github account
* spyder (optional): Integrated development environment (IDE) for Python
* jupyter (optional)


