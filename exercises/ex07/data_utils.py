"""Utility functions."""

__author__ = "730521799"

# Define your functions below


from csv import DictReader


# Read CSV Files
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Function that reads csv files in a list."""
    result: list[dict[str, str]] = []

    # Open File
    file_handle = open(filename, "r", encoding="utf8")

    # Open a handle
    csv_reader = DictReader(file_handle)

    # Read each row
    for row in csv_reader:
        result.append(row)

    # Close file
    file_handle.close()

    return result


# Creates a list
def column_values(x: list[dict[str, str]], y: str) -> list[str]:
    """Function that creates a list with column values."""

    # Empty List
    list_1: list[str] = []

    # Loop
    for item in x:
        if y in item:
            list_1.append(item[y])

    # Return
    return list_1


# Transform list in a table with columns
def columnar(x: list[dict[str, str]]) -> dict[str, list[str]]:
    """List to columns."""

    # Dict value
    result: dict[str, list[str]] = {}

    # Row value
    first_row: dict[str, str] = x[0]
    for column in first_row:
        result[column] = column_values(x, column)
    
    return result


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Number of columns only."""

    # Dict value
    result: dict[str, list[str]] = {}

    list_1: list[str] = []

    for item in x:
        # Counter value
        i: int = 0
        while i < y and i < len(x[item]):
            list_1.append(x[item][i])
            i = i + 1
    
    return result


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Select columns"""
    result: dict[str, list[str]] = {}

    # Add item
    for item in y:
        result[item] = x[item]
    
    return result
        

def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Add values to dict."""
    result: dict[str, list[str]] = {}

    # For Dict x
    for item in x:
        result[item] = x[item]
    
    # For Dict y
    for item in y:
        if item in result:
            for item_b in y[item]:
                result[item].append(item_b)
        
        else:
            result[item] = y[item]

    return result


def count(x: list[str]) -> dict[str, int]:
    """Find number of times in a dict."""
    result: dict[str, int] = {}

    # Add Values
    for item in x:

        if item in result:
            result[item] += 1
        else:
            result[item] = 0
            result[item] += 1
    
    return result
