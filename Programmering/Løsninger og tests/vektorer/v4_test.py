from v4 import *
from pytest import raises

def test_sum_of_squared_positives():
    v = [3, -2, 7, 1, -4]
    # -2 og -4 burde sorteres fra
    # kvadrattallene for resten burde være 9, 49, 1
    # sum = 59
    assert sum_of(squared(positives_of(v))) == 59


def test_root_login_pipeline():
    logs = [
        {"username": "root", "timestamp": 100, "success": False},
        {"username": "alice", "timestamp": 105, "success": True},
        {"username": "root", "timestamp": 110, "success": True},
        {"username": "root", "timestamp": 115, "success": False},
    ]

    # 1. filtrering
    root_attempts = root_login_attempts_of(logs)
    assert len(root_attempts) == 3
    assert all(entry["username"] == "root" for entry in root_attempts)

    # 2. afbildning
    ts_success = timestamps_of_with_success(root_attempts)
    assert ts_success == [(100, False), (110, True), (115, False)]

    # 3. reduktion
    first, last, failures, successes = summary_of(ts_success)
    assert first == 100
    assert last == 115
    assert failures == 2
    assert successes == 1

def test_summary_of_empty():
    with raises(ValueError):
        summary_of([])


def test_one_liners():
    v = [3, -2, 7, 1, -4]
    assert positives_of_one_liner(v) == [3, 7, 1]
    assert squared_one_liner([3, 7, 1]) == [9, 49, 1]
    assert sum_of_one_liner([9, 49, 1]) == 59
    assert sum_of_squared_positives_one_liner(v) == 59


def test_reduce_versions():
    assert sum_of_reduce([3, -2, 7, 1, -4]) == 5
    assert sum_of_reduce([]) == 0

    assert prod_of_reduce([3, -2, 7]) == -42
    assert prod_of_reduce([]) == 1

    assert max_of_reduce([3, -2, 7, 1, -4]) == 7
    
    with raises(ValueError):
        max_of_reduce([])