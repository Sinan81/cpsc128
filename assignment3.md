# Assignment 3

This assignment is due Monday June 3rd, although I strongly encourage early submission. Remember to implement the best programming practices: meta info, comments, readability (naming of variables and constants), and user interaction. Also, use single spaces around the relational and logical operators, and the assignment operator '=' to improve readability.

Before working on questions 2 & 3, you might want to check out "working with lists" section of the python cheat sheet or relevant slides from the class.


## 1. Drawing Diamonds

Write a program that displays a diamond on the screen, e.g.

        *
       * *
      * * *
     * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
Your program should ask the user how large a diamond to draw and what character to use to draw it. (The size of a diamond is specified by the lengths of its sides, i.e. 5 in the case above).

You can use any `print()` tricks in this question if you like, although they are not necessary. For example, `print(n*mystr)` where a character or a string `mystr` is printed multiple times in the same line. As before you might also want to use `print(mystr, end='')` trick to continue printing in the same line.


## 2. Dedup

Write two versions of a Python script that removes duplicate values from a list. If the list starts out as `[4, 2, 5, 2, 4]`, then after your code fragment runs it should be like:

i.  `[5, 2, 4]` in version-1 where the left most duplicates are removed first

ii. `[4, 2, 5]` in version-2 where the right most duplicates are removed first

In both versions, the original list, the deduplicated list, as well as  a sorted version of deduplicated list should be outputted.

(A real-life application would be to remove duplicates from a list of IP addresses so you have a list of unique visitors to your site. In this case the list might look like `[ '10.9.0.31', '199.247.52.3', '10.9.0.31', '43.98.12.4', '72.1.3.55', '199.247.52.3', ...]).

Hint: No user interaction is expected in this exercise, hence you might want to use `random.randint()` to generate a random list to work with. You can put both versions in the same *.py file if you like.


## 3. Handy List Program

This program first takes a list input in the form a single string.
Afterwards, it continues to take string input and checks if that string is in a list of strings

* if string is in the list it removes the first instance from list
* if string is not in the list the input gets appended to the list
* if the string is empty then the last item is popped from the list
* if the list becomes empty the program ends
* if the user enters "quit" then the program ends

Sample run 1:
```
-----------------------
handy_list_tool version 0.1
-----------------------
Enter a non-empty list like ['cat', 'dog']
['cat', 'dog', 'cat']

the list is:  ['cat', 'dog', 'cat']
Enter the name of animal: horse
1 instance of horse appended to list

the list is:  ['cat', 'dog', 'cat', 'horse']
Enter the name of animal: cat
1 instance of cat removed from list

the list is:  ['dog', 'cat', 'horse']
Enter the name of animal:     <-- pressed Enter here (i.e. empty string)
horse popped from the list

the list is:  ['dog', 'cat']
Enter the name of animal:     <-- pressed Enter here (i.e. empty string)
cat popped from the list

the list is:  ['dog']
Enter the name of animal:     <-- pressed Enter here (i.e. empty string)
dog popped from the list
Goodbye!
```

Sample run 2:
```
-----------------------
handy_list_tool version 0.1
-----------------------
Enter a non-empty list like ['cat', 'dog']
['cat', 'whale']

the list is:  ['cat', 'whale']
Enter the name of animal: quit
Goodbye!
```

Sample run 3:
```
-----------------------
handy_list_tool version 0.1
-----------------------
Enter a non-empty list like ['cat', 'dog']
Quit
Goodbye!
```

Hint: You might want to use `input()` to read in everything as a string as opposed to what we usually do `eval(input(...))`. Also, you might want to use `eval()` in the very beginning of the program to convert the inputted string to a list:
```python
In [21]: x = input()

['cat', 'dog']

In [22]: print(type(x), x)
<class 'str'> ['cat', 'dog']

In [23]: y = eval(x)

In [24]: print(type(y), y)
<class 'list'> ['cat', 'dog']
```

**Credits**: The original source of this programming exercise to be revealed in the end of the course.













