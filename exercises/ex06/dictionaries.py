"""Practice with dictionaries."""

__author__ = "730521799"

# Define your functions below


# Function 1 Invert
def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert Dictionary."""
    dict_1: dict[str, str] = {}
    dict_1 = {v: k for k, v in x.items()}
    return dict_1


# Function 2 Favorite colors
def favorite_color(x: dict[str, str]) -> str:
    """Find duplicates in Dictionary."""
    dict_2: dict[str, int] = {}
    for item in x:
        if (x[item] in dict_2) is True:
            dict_2[x[item]] += 1
        else:
            dict_2[x[item]] = 1
    return max(dict_2, key=dict_2.get)


# Function 3 Count
def count(x: list[str]) -> dict[str, int]:
    """Dictionary with values using another Dictionary."""
    dict_3: dict[str, int] = {}
    for item in x:
        if (item in dict_3) is True:
            dict_3[item] += 1
        else:
            dict_3[item] = 1
    return(dict_3)


print(invert({'a': 'z', 'b': 'y', 'c': 'x'}))

print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Mark": "yellow"}))

print(count(["blue", "yellow", "blue", "blue", "green"]))