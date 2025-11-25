from v5 import *

# Opgave 1
def test_cum_sum_of():
    assert cum_sum_of([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert cum_sum_of([]) == []
    assert cum_sum_of([5]) == [5]
    assert cum_sum_of([-1, -2, 3]) == [-1, -3, 0]

# Opgave 2
def test_cum_max_of():
    assert cum_max_of([2, -3, 4, 8, 7]) == [2, 2, 4, 8, 8]
    assert cum_max_of([]) == []
    assert cum_max_of([5, 5, 5]) == [5, 5, 5]
    assert cum_max_of([-2, -5, -1]) == [-2, -2, -1]

# Opgave 3
def test_cum_union_of():
    inp = [{2, 3}, {2, 4}, {3}, {3, 6}]
    out = [{2, 3}, {2, 3, 4}, {2, 3, 4}, {2, 3, 4, 6}]
    assert cum_union_of(inp) == out
    assert cum_union_of([]) == []
    assert cum_union_of([set()]) == [set()]

# Opgave 4
def test_make_cumulative():
    cum_sum = make_cumulative(lambda a, b: a + b, 0)
    assert cum_sum ([1, 2, 3]) == [1, 3, 6]

    cum_max = make_cumulative(lambda a, b: a if a > b else b, float("-inf"))
    assert cum_max([2, -3, 4, 8, 7]) == [2, 2, 4, 8, 8]

    cum_prod = make_cumulative(lambda a, b: a * b, 1)
    assert cum_prod([2, 3, 4]) == [2, 6, 24]

# Opgave 5
def test_cum_avg_of():
    assert cum_avg_of([2, -3, 4, 8, 7]) == [2.0, -0.5, 1.0, 2.75, 3.6]
    assert cum_avg_of([]) == []
    assert cum_avg_of([5]) == [5.0]

# Opgave 6
def test_moving_avg_of():
    inp = [2, -3, 4, 8, 6]    
    assert moving_avg_of(inp) == [2.0, -0.5, 1.0, 3.0, 6.0]
    assert moving_avg_of([]) == []
    assert moving_avg_of([1, 2, 3, 4], window=2) == [1.0, 1.5, 2.5, 3.5]

# Opgave 7
def test_daily_ohlc():
    data = [
        ('2025-01-14', '10:03', 74),
        ('2025-01-14', '12:27', 94),
        ('2025-01-14', '15:42', 64),
        ('2025-01-14', '17:12', 84),
        ('2025-01-15', '09:39', 75),
        ('2025-01-15', '13:18', 85),
    ]
    expected = [
        ('2025-01-14', 74, 94, 64, 84),
        ('2025-01-15', 75, 85, 75, 85),
    ]
    assert daily_ohlc(data) == expected
    assert daily_ohlc([]) == []
    assert daily_ohlc([('2025-02-01', '08:00', 100)]) == [('2025-02-01', 100, 100, 100, 100)]

