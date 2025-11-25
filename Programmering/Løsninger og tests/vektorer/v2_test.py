from v2 import *


def test_doubled():
    assert doubled([3, -2, 7, 1, -4]) == [6, -4, 14, 2, -8]
    assert doubled([]) == []
    assert doubled([0, 5]) == [0, 10]


def test_squared():
    assert squared([3, -2, 7, 1, -4]) == [9, 4, 49, 1, 16]
    assert squared([0, 5, -3]) == [0, 25, 9]
    assert squared([]) == []


def test_lengths():
    data = ["fuck", "you", "", "🙂"]
    assert length(data) == [4, 3, 0, 1]
    assert length([]) == []
    assert length(["a", "ab", "abc"]) == [1, 2, 3]


def test_decrement():
    data = [3, -2, 7, 1, -4]
    decrement(data)
    assert data == [2, -3, 6, 0, -5]

    empty = []
    decrement(empty)
    assert empty == []

    single = [0]
    decrement(single)
    assert single == [-1]


def test_add_danish_vat():
    prices = [100.0, 20, 0, 8.8]
    add_danish_vat(prices)
    # round for lettere læsning/skrivning
    assert [round(p, 2) for p in prices] == [125.00, 25.00, 0.00, 11.00]

    empty = []
    add_danish_vat(empty)
    assert empty == []


def test_negate():
    flags = [True, False, True, True, False]
    negate(flags)
    assert flags == [False, True, False, False, True]
    
    empty = []
    negate(empty)
    assert empty == []

    all_true = [True, True]
    negate(all_true)
    assert all_true == [False, False]