# CPSC128
This is a repository for the CPSCS 128 "Introductory Programming using Python" course.

See the syllabus: [CPSC 128 Spring 2018-19 Syllabus](files/CPSC_128_outline_2019.pdf)

## Lecture Notes (by Tim Topper)
In this course, to a significant extent I will be following previous instructor's (Tim Topper) contents. Accordingly, you might find his lecture notes useful:

[Lecture Notes](files/CPSC128.spring2018-19/)

After clonin this repository to your computer open the following file on an internet browser: `files/CPSC128.spring2018-19/index.html`

## Assignments

[Assignment 1](assignment1.md) Due May 20, Monday

[Assignment 2](assignment2.ipynb) Due May 24, Friday

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

[May  2](files/cpsc128_slides_may2.pdf)

[May  7](files/cpsc128_slides_may7.pdf)

[May  9](files/cpsc128_slides_may9.pdf)

[May 14](files/cpsc128_slides_may14.pdf)

[May 16](files/cpsc128_slides_may16.pdf)

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
```
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
    again = raw_input( "Play again (y/n)? " )
print("Thanks for playing")
```


## github Markdown (optional)

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

## Computing Setup

* python3
* git: version control
* github account
* spyder (optional): Integrated development environment (IDE) for Python
* jupyter (optional)


