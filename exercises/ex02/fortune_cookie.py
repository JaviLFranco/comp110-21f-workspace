"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730521799"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


value = randint(1, 10)
print("Your fortune cookie says...")

if value > 2:
    if 5 > value > 2:
        print("Isn't there something else you should be working on right now?")
    if 8 > value >= 5:
        print("The life of every woman or man - the heart of it - is pure and holy joy.")
    if value >= 8:
        print("Adversity is the parent of virtue.")

else:
    print("The man who waits till tomorrow, misses the opportunities of today.")
print("Now, go spread positive vibes!")