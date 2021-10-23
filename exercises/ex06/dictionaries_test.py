"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730521799"

from ex06.dictionaries import invert
from ex06.dictionaries import favorite_color
from ex06.dictionaries import count


# Test 1 for invert
def test_invert_result_a() -> None:
    """Return inverted value 1."""
    x: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert "z" in invert(x)


# Test 2 for invert
def test_invert_result_b() -> None:
    """Return inverted value 2."""
    x: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert "y" in invert(x)


# Test 3 for invert
def test_invert_result_c() -> None:
    """Return inverted values."""
    x: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(x) == {'z': 'a', 'y': 'b', 'x': 'c'}


# Test 1 for favorite_color
def test_favorite_color_result_a() -> None:
    """Return max value 1."""
    x: dict[str, str] = {"Marc": "green", "Ezri": "blue", "Kris": "green", "Mark": "green"}
    assert favorite_color(x) == "green"


# Test 2 for favorite_color
def test_favorite_color_result_b() -> None:
    """Return max value 2."""
    x: dict[str, str] = {"Marc": "green", "Ezri": "blue", "Kris": "blue", "Mark": "yellow"}
    assert favorite_color(x) == "blue"


# Test 3 for favorite_color
def test_favorite_color_result_c() -> None:
    """Return max value 3."""
    x: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Mark": "yellow"}
    assert favorite_color(x) == "yellow"


# Test 1 for count
def test_count_result_a() -> None:
    """Return inverted value 1."""
    x: list[str] = ["blue", "yellow", "blue", "blue", "green"]
    assert "green" in count(x)


# Test 2 for count
def test_count_result_b() -> None:
    """Return inverted value 2."""
    x: list[str] = ["blue", "yellow", "blue", "blue", "green"]
    assert "blue" in count(x)


# Test 3 for count
def test_count_result_c() -> None:
    """Return inverted values."""
    x: list[str] = ["blue", "yellow", "blue", "blue", "green"]
    assert count(x) == {'blue': 3, 'yellow': 1, 'green': 1}