"""Counting letters in a string."""

__author__ = "730521799"


letter: str = input("What letter do you want to seach for?: ")
word: str = input("Enter a word: ")
i = 0
count = 0

while(i < len(word)):
    if(word[i] == letter):
        count = count + 1
    i = i + 1

print(("Count: ") + str(count))