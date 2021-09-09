"""Repeating a beat in a loop."""

__author__ = "730521799"


beat: str = input("What beat do you want to repeat? ")
times: str = input("How many times do you want to repeat it? ")
tb = int(times)
tc = tb
space: str = ' '

if tb > 0:
    while tb == tc: 
        print((tb - 1) * (beat + space) + beat) 
        tb = tb - 1
else:
    print("No beat...")