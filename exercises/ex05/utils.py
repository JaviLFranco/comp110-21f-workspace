"""List utility functions part 2."""

__author__ = "730521799"

# Define your functions below


def only_evens(x: list) -> list:
    """Return list with only evens."""
    list_1: list = []
    for item in x:
        if (item % 2) == 0:
            list_1.append(item)
    return list_1


def sub(x: list, y: int, z: int) -> list:
    """Return list with only chosen values."""
    list_2: list = []
    for item in x:
        if x[y] <= item <= x[z - 1]:
            list_2.append(item)
    return list_2


def concat(x: list, y: list) -> list:
    """Sum both lists."""
    list_3: list = []
    for item in x:
        list_3.append(item)
    for item in y:
        list_3.append(item)
    return list_3


print(only_evens([1, 2, 4]))

a_list = [10, 20, 30, 40]
print(sub(a_list, 1, 4))

print(concat([1, 2, 3], [4, 7, 9]))