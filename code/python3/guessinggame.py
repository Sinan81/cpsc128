# guessinggame.py
# CPSC128 Exercise
# 

print("Guessing game!")

target = random.randint(1,100)
guess = 0 #initialize
n=0
while guess != target:
    guess = eval(input('enter guess\n'))
    if guess < target:
        print("your guess is low")
    elif guess > target:
        print("your guess is high")
    else:
        print("Congrats you guessed the value correctly!")
    n=n+1

print("total guesses: ",n)     