# Assignment 1
This assignment is due by Monday May 20th although I encourage early submission. In your python programs, please follow the programming best practices we discussed in the class.

## Trivialities

We only know enough Python commands to write simple programs so far, but we do need to practice using what we've got so ... write a program that produces sessions like this one:

```
Useless Trivia Generator v0.01
==============================
How old are you? 28
And how many pounds do you weigh? 165
Did you know that you're 196 in dog years!
But you're also over 883008000 seconds old.
Did you know that on the moon you would weigh only 27.5 pounds?
But on the sun, you'd weigh 4471.5 pounds (but not for long!).
```

Some facts that might be helpful to you in writing your program:

* There are seven dog years in each calendar year.
* There are 60 seconds in a minute, 60 minutes in an hour, 24 hours in a day, and (at least) 365 days in a year.
* Things weigh 1/6th as much on the moon as they do on the surface of the earth.
* Things weigh 27.1 times as much on the surface of the sun as they do on the surface of the earth.

## Calculating Wind Chill
While the temperature tells us how cold the air outside is, we are often more interested in how quickly we will cool down. The rate at which we lose heat depends on the temperature outside, and also on the speed of the wind: the combined effect of temperature and wind speed is often called the wind chill. The effective temperature, *T*<sub>e</sub>, can be calculated using the expression,

*Te = 13.12 + 0.6215 T - 11.37 x V<sup>0.16</sup> + 0.3965 x T x V<sup>0.16</sup>*

where *V* is the wind speed in kilometres per hour, and *T* is the temperature in Celsius.

Write a program that calculates the effective temperature. It should request the temperature and wind speed from the user and output the effective temperature.

##    Converting from furlongs et al to feet

A historian has come across a large body of material using outdated units of measurement. Specifically, distance measurements are given in terms of feet, yards (1 yard = 3 feet), chains (1 chain = 22 yards), and furlongs (1 furlong = 10 chains). Write a program that will let her enter one of the historical measurements in furlongs, chains, yards and feet (e.g. 2 furlongs, 3 chains, 13 yards and 2 feet) and output the equivalent measurement in feet (i.e. 1559 feet).

##    Converting from feet to furlongs et al

The historian above now wishes to convert some measurements she has made in feet into these archaic units. Write a program that will convert from feet to furlongs, chains, yards and feet, so if she inputs 1559 the output should be something like:

```
1559 feet is equal to:
2 furlongs,
3 chains,
13 yards, and
2 feet.
```

## Logistics

Submit your assignment by emailing your python programs to me as a single *.zip file.

## Copyright

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. This content was originally created by Dr. Tim Topper.
