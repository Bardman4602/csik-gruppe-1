from v3 import *
from pytest import raises

def test_sum_of():
    assert sum_of([3, -2, 7, 1, -4]) == 5
    assert sum_of([]) == 0
    assert sum_of([0, 0, 0]) == 0
    assert sum_of([-1, -2, -3]) == -6


def test_prod_of():
    assert prod_of([3, -2, 7, 1, -4]) == 168
    assert prod_of([]) == 1
    assert prod_of([5]) == 5
    assert prod_of([0, 1, 2]) == 0


def test_concat_of():
    assert concat_of(["a", "bc", "def"]) == "abcdef"
    assert concat_of([]) == ""
    assert concat_of(["", "x", ""]) == "x"


def test_all_of():
    assert all_of([True, True, True]) is True
    assert all_of([True, False, True]) is False
    assert all_of([]) is True
    assert all_of([False, False]) is False


def test_any_of():
    assert any_of([False, False, True]) is True
    assert any_of([False, False, False]) is False
    assert any_of([]) is False
    assert any_of([True, False]) is True


def test_max_of():
    assert max_of([3, -2, 7, 1, -4]) == 7
    assert max_of([-10, -20, -5]) == -5
    assert max_of([42]) == 42
    with raises(ValueError):
        max_of([])


def test_shortest_of():
    assert shortest_of(["abc", "d", "efgh", "ij"]) == "d"
    assert shortest_of(["same", "size", "here"]) == "same"
    assert shortest_of(["longer", "short"]) == "short"
    with raises(ValueError):
        shortest_of([])


def test_avg_of():    
    assert avg_of([1, 2, 3, 4]) == 2.5
    assert avg_of([-2, 2]) == 0.0
    assert avg_of([5]) == 5.0
    with raises(ValueError):
        avg_of([])


def test_separated_sum_of():
    assert separated_sum_of([3, -2, 7, -1, 0]) == (10, -3)
    assert separated_sum_of([]) == (0, 0)
    assert separated_sum_of([0, 0, 0]) == (0, 0)
    assert separated_sum_of([-5, -5]) == (0, -10)
    assert separated_sum_of([5, 5]) == (10, 0)