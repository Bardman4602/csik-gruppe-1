from v1 import *

# Opg 1
def test_positives_of():
    assert positives_of([3, -2, 7, 1, -4]) == [3, 7, 1]
    assert positives_of([]) == []
    assert positives_of([-5, -1]) == []
    assert positives_of([0, 2, 3]) == [2, 3]

#Opg 2
def test_non_empty_of():
    inp = ["hello", "", "world", "", "!", ""]
    exp = ["hello", "world", "!"]
    assert non_empty_of(inp) == exp
    assert non_empty_of([]) == []
    assert non_empty_of([""]) == []

#opg 3
def test_suspicious_login_attempts_of():
    data = [
        ("2025-10-30T07:25:14", "root",  False),
        ("2025-10-30T07:26:04", "admin", False),
        ("2025-10-30T07:27:00", "root",  True ),
        ("2025-10-30T07:28:14", "root",  False) 
    ]
    expected = [
        ("2025-10-30T07:25:14", "root", False),
        ("2025-10-30T07:28:14", "root", False)
    ]
    
    assert suspicious_login_attempts_of(data) == expected
    assert suspicious_login_attempts_of([]) == []

def test_every_second_char_of():
    assert every_second_char_of("abcdef") == ["a", "c", "e"]
    assert every_second_char_of("a") == ["a"]
    assert every_second_char_of("") == []
    assert every_second_char_of("12345") == ["1", "3", "5"]

def test_remove_negatives():
    data = [3, 2, 7, 1, -4]
    remove_negatives(data)
    assert data == [3, 2, 7, 1]

    data = [-5, -1, -9]
    remove_negatives(data)
    assert data == []

    data = [0, 2, 5]
    remove_negatives(data)
    assert data == [0, 2, 5]

def test_remove_empty():
    data = ["hello", "", "world", "", "!"]
    remove_empty(data)
    assert data == ["hello", "world", "!"]

    data = ["", "", ""]
    remove_empty(data)
    assert data == []

    data = ["a", "b"]
    remove_empty(data)
    assert data == ["a", "b"]

def test_remove_every_other():
    data = [0, 1, 2, 3, 4, 5]
    remove_every_other(data)
    assert data == [1, 3, 5]

    data = ["a"]
    remove_every_other(data)
    assert data == []

    data = []
    remove_every_other(data)
    assert data == []