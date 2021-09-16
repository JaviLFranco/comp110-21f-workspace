"""An exercise in remainders and boolean logic."""

__author__ = "730521799"


value = int(input("Enter an int: "))

if (value % 2) == 0:
    if (value % 7) == 0:
        print("TAR HEELS")
    else: 
        print("TAR")
if (value % 7) == 0:
    if (value % 2) != 0:
        print("HEELS")
if (value % 2) != 0:
    if (value % 7) != 0:
        print("CAROLINA")