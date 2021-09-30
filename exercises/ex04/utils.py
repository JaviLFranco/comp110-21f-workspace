"""List utility functions."""

__author__ = "730521799"


# TODO: Implement your functions here.
def all(x: list, y: int) -> bool:
    if y in x:
        return True
    else:
        return False


def is_equal(x: list, y: list) -> bool:
    if x == y:
        return True
    else:
        return False


def max(input: list) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        """Return max value"""
        i: int = 0
        max_value: int = input[0]
        while i < len(input):
            if max_value < input[i]:
                max_value = input[i]
            i += 1
        return max_value


print(all([1, 2, 3], 1))

print(is_equal([1, 2, 3], [1, 2, 3]))

print(max([1000, 100, 10]))