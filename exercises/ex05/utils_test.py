"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730521799"


from ex05.utils import only_evens
from ex05.utils import sub
from ex05.utils import concat


def test_only_evens_result() -> None:
    """Return list with only evens."""
    x: list[int] = [1, 2, 3]
    assert only_evens(x) == [2]


def test_only_evens_result_b() -> None:
    """Return list with only evens."""
    x: list[int] = [1, 2, 4]
    assert only_evens(x) == [2, 4]


def test_only_evens_result_c() -> None:
    """Return list with only evens."""
    x: list[int] = [1, 3, 7]
    assert only_evens(x) == []


def test_sub_result() -> None:
    """Return list with only chosen values."""
    x: list[int] = [10, 20, 30, 40]
    y: int = 1
    z: int = 4
    assert sub(x, y, z) == [20, 30, 40]


def test_sub_result_b() -> None:
    """Return list with only chosen values."""
    x: list[int] = [10, 20, 30, 40]
    y: int = 0
    z: int = 2
    assert sub(x, y, z) == [10, 20]


def test_sub_result_c() -> None:
    """Return list with only chosen values."""
    x: list[int] = [10, 20, 30, 40]
    y: int = 1
    z: int = 2
    assert sub(x, y, z) == [20]


def test_concat_result() -> None:
    """Sum both lists."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 7, 10]
    assert concat(x, y) == [1, 2, 3, 4, 7, 10]


def test_concat_result_b() -> None:
    """Sum both lists."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 6, 9]
    assert concat(x, y) == [1, 2, 3, 4, 6, 9]


def test_concat_result_c() -> None:
    """Sum both lists."""
    x: list[int] = [1, 2, 4]
    y: list[int] = [5, 7, 9]
    assert concat(x, y) == [1, 2, 4, 5, 7, 9]