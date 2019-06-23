# Assignment 6, Due June 24th Monday
This is an assignment on Object Oriented Programming. Note that this is the last assignment of the course. It might be a good idea to complete problems in the order of: Problem 1, 3, and 2.

## Problem-1 A little class of your own
Write a Coin class that will enable this code to run,
```python

# Your class goes here...

if __name__ == '__main__':
    coin = Coin()
    print('Your first coin is a %s.' % (coin))

    purse = [coin]
    print('Adding four more coins to your purse...')
    for i in range(4):
        coin = Coin(random.choice([1,5,10,25,100,200]))
        purse.append(coin)

    print('In your purse you now have:')
    for coin in purse:
        print('\ta', coin)

    total = 0
    for coin in purse:
        total += coin.value
    print('The total value of the coins in your purse is', total, 'cents.')

    print('Flipping your coins you get: ', end='')
    for coin in purse:
        print(coin.flip(),' ', end='')
```
and produce this output:
```
Your first coin is a Penny.
Adding four more coins to your purse...
In your purse you now have:
        a Penny
        a Nickel
        a Toonie
        a Toonie
        a Quarter
The total value of the coins in your purse is 431 cents.
Flipping your coins you get: Head  Tail  Head  Tail  Tail
```
Remember  that `print` method can print an object only if `__str__` method is defined within the associated class. Also, `__str__` method is expected to return a value of `str` type.

## Problem 2 Hunt the Wumpus game

As a reference, a good implementation of this game can be found at [https://www.ifiction.org](https://www.ifiction.org/games/playz.php?cat=1&game=249&mode=html)

### 2A Complete the code to create a working Hunt the Wumpus program

Complete [`wumpus_4_partial.py`](code/python3/wumpus_4_partial.py) to create a working Hunt the Wumpus program, i.e. you should fix the bugs, if there is any, and add the necessary new code. Make as few changes to the code as possible. Ideally you will just make additions to it.

### 2B Add a feature to Hunt the Wumpus, e.g.

Add one of the following features via adding to or modifying Hunt the Wumpus program.

* Add a new hazard type, e.g. riddlesand, like quicksand you sink into it, but you can save yourself if you can guess the secret number (from 1 to 10) in three tries.

* Add extra arrows in some of the rooms that get automatically added to your quiver when you enter the room.

* Have the Wumpus start out sleepy with a 0.75 chance of being startled and running away, but as the game progresses have the Wumpus become more alert and more likely to eat the player.

* A limited number of moves in which to finish the game


Your mark will reflect the scope of your additions, and the quality of your code. Be sure to describe the changes in your comments so I do not overlook them when I run your program, and be sure to add any "cheat" information needed to make them easy to test.

## Problem 3 CoinJar class

The class CoinJar represents a jar of Canadian coins. Write the necessary code so this program will run correctly. 

```python
tims = CoinJar(pennies = 3, quarters = 2, loonies = 1)
mollys = CoinJar(pennies = 48, nickels = 12, dimes = 7, quarters = 14)
print(tims.value()) # Displays 1.53
print(mollys.value() ) # Displays 5.28
print(tims.dimes) # Displays 0.
print(tims[0]) # Displays 0 
print(mollys.quarters) # Displays 14.
print(mollys[5]) # Displays 48.
if tims > mollys:
    print('Tim is richer than Molly.')
else:
    print('Molly is at least as rich as Tim.')
# ^ Displays: Molly is at least as rich as Tim.

tims = tims + mollys
print(tims)
```
*Hint*: Since the order of the parameters varies between the two constructor calls in lines 1 and 2 we can tell that *named parameters* are being used (_see the brief discussion in Python cheats_). Also, the number of parameters indicated for two constructors at lines 1 and 2 are different, hence it is implicit that unspecified input parameters should default to a predefined value.





