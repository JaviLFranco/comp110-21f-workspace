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


print("Your fortune cookie says...")

if randint(1, 10) > 5:
    print("Isn't there something else you should be working on right now?")
else:
    print("The man who waits till tomorrow, misses the opportunities of today.")
print("Now, go spread positive vibes!")