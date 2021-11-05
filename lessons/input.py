"""Examples of user inputs and variables."""

print("Wow, " + input("Hey, who are you? ") + ", you rock!")
print(input("Who are you? ") + ", have a great day!")


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    "Number of columns only."

    # Dict value
    result: dict[str, list[str]] = {}

    list_1: list[str] = []

    for column in x:
        # Counter value
        i: int = 0
        while i < y and i < len(x[column]):
            list_1.append(x[column][i])
            i = i + 1
    
    return result



def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Select columns"""
    result: dict[str, list[str]] = {}

    # Add item
    for item in y:
        result[item] = x[item]
    
    return result