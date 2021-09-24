"""Battle Creatures."""

__author__ = "730521799"

from random import randint

TREE: str = '\U0001F332'

points: int = 100
life_o: int = 100
power_o: int = 15
attack_o: str = "Z"


def greet() -> None:  
    player: str = input("What is your name? ")
    print("Welcome to Battle Creatures, " + player)


greet()


def main() -> None:
    creature_name: str = input("What is the name of your creature? ")
    print(creature_name + " is a great name!")
    legs: int = int(input("How many legs does " + creature_name + " have? "))
    arms: int = int(input("How many arms does " + creature_name + " have? "))
    speed: int = 0
    strenght: int = 0
    life_o: int = 100
    attack_o: str = "Z"
    opponent_name: str = input("What is your opponent's name? ")

    if legs < 2:
        speed: int = 1
    
    if 2 <= legs <= 4:
        speed: int = 10

    if legs > 4:
        speed: int = 3

    print(creature_name + " has a speed of " + str(speed))

    if arms < 2:
        strenght: int = 1
    
    if 2 <= arms <= 4:
        strenght: int = 10

    if 4 < arms:
        strenght: int = 3

    print(creature_name + " has a strenght of " + str(strenght))

    power: int = (speed + strenght)

    points: int = 0

    if power < 10:
        points: int = 130
    
    if 10 <= power <= 15:
        points: int = 115

    if 15 < power:
        points: int = 100

    print(creature_name + " has an attack power of " + str(power) + " and a life of " + str(points))

    while points > 0:
        if int(life_o) > 0:
            print("What attack do you want to use?")
            print(" A - Fire Attack")
            print(" B - Plant Attack")
            print(" C - Water Attack")

            attack: str = input("Enter a letter: ")

            value = randint(1, 9)

            if value <= 3:
                attack_o: str = "A"
    
            if 3 < value <= 6:
                attack_o: str = "B"

            if 6 < value:
                attack_o: str = "C"

            if attack == "A":
                if attack_o == "A":
                    print(creature_name + "'s attack is neutralized by your opponent.")
                if attack_o == "B":
                    print(creature_name + " uses a fire attack. Your opponent loses " + str(power) + " life points.")
                    life_o: int = life_o - power
                if attack_o == "C":
                    print(creature_name + "'s attack is neutralized by your opponent. Your opponent uses a water attack. Your creature loses " + str(power_o) + " life points.")
                    points: int = points - power_o

                print(str(creature_name) + " has " + str(points) + " life points.")
                print(opponent_name + " has " + str(life_o) + " life points.")

            if attack == "B":
                if attack_o == "B":
                    print(creature_name + "'s attack is neutralized by your opponent.")
                if attack_o == "C":
                    print(creature_name + " uses a plant attack. Your opponent loses " + str(power) + " life points.")
                    life_o: int = life_o - power
                if attack_o == "A":
                    print(creature_name + "'s attack is neutralized by your opponent. Your opponent uses a fire attack. Your creature loses " + str(power_o) + " life points.")
                    points: int = points - power_o

                print(str(creature_name) + " has " + str(points) + " life points.")
                print(opponent_name + " has " + str(life_o) + " life points.")

            if attack == "C":
                if attack_o == "C":
                    print(creature_name + "'s attack is neutralized by your opponent.")
                if attack_o == "A":
                    print(creature_name + " uses a water attack. Your opponent loses " + str(power) + " life points.")
                    life_o: int = life_o - power
                if attack_o == "B":
                    print(creature_name + "'s attack is neutralized by your opponent. Your opponent uses a plant attack. Your creature loses " + str(power_o) + " life points.")
                    points: int = points - power_o

                print(str(creature_name) + " has " + str(points) + " life points.")
                print(opponent_name + " has " + str(life_o) + " life points.")

            points_b = points

        else:
            print("Well done, " + creature_name + " beat its opponent. The opponent fled to the woods. " + TREE * 3)
            points = points - points

    if points_b < 1:
        print("GAME OVER: the opponent beat " + creature_name + ". " + creature_name + " fled to the woods. " + TREE * 3)


if __name__ == "__main__":
    main()