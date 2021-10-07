"""List utility functions part 2."""

__author__ = "730521799"

# Define your functions below


def only_evens(x: list[int]) -> list[int]:
    """Return list with only evens."""
    list_1: list[int] = []
    for item in x:
        if (item % 2) == 0:
            list_1.append(item)
    return list_1


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Return list with only chosen values."""
    list_2: list[int] = []
    if len(x) == 0:
        return list_2
    else:
        for item in x:
            if x[y] <= item <= x[z - 1]:
                list_2.append(item)
        return list_2


def concat(x: list[int], y: list[int]) -> list:
    """Sum both lists."""
    list_3: list[int] = []
    for item in x:
        list_3.append(item)
    for item in y:
        list_3.append(item)
    return list_3


print(only_evens([1, 2, 4]))

a_list = [10, 20, 30, 40]
print(sub(a_list, 1, 4))

print(concat([1, 2, 3], [4, 7, 9]))