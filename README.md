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

- import a module/library and use a method from this module:

```
import math

math.sqrt(9)
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


