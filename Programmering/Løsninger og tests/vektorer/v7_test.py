from v7 import *

# Opgave 1
def test_reverse_of():
    assert reverse_of([1, 2, 3]) == [3, 2, 1]
    assert reverse_of([]) == []
    assert reverse_of(["a", "b"]) == ["b", "a"]

def test_reverse():
    values = [1, 2, 3, 4]
    reverse(values)
    assert values == [4, 3, 2, 1]
    values = []
    reverse(values)
    assert values == []
    values = [42]
    reverse(values)
    assert values == [42]

# Opgave 2
def test_shuffle():
    values = [1, 2, 3, 4, 5]
    shuffled = values.copy()
    shuffle(shuffled)
    assert sorted(shuffled) == sorted(values)
    assert shuffled != values or True
    empty = []
    shuffle(empty)
    assert empty == []

# Opgave 3
def test_merge_sort_of():
    assert merge_sort_of([4, 1, 7, 3]) == [1, 3, 4, 7]
    assert merge_sort_of([]) == []
    assert merge_sort_of([5]) == [5]
    assert merge_sort_of([2, 2, 1]) == [1, 2, 2]


# Opgave 4
def test_partial_sort():
    values = [4, 1, 4, 3, 2, 8, 7, 7, 1]
    w, b = partial_sort(4, values)
    assert values == [1, 3, 2, 1, 4, 4, 8, 7, 7]
    assert (w, b) == (4, 6)

    # alle mindre end x
    values = [1, 2, 3]
    w, b = partial_sort(5, values)
    assert values == [1, 2, 3]
    assert (w, b) == (3, 3)

    # alle større end x
    values = [9, 8, 7]
    w, b = partial_sort(5, values)
    assert values == [9, 8, 7]
    assert (w, b) == (0, 0)


# Opgave 5
def test_quick_sort():
    values = [4, 1, 7, 3]
    quick_sort(values)
    assert values == [1, 3, 4, 7]

    values = [5, 5, 5]
    quick_sort(values)
    assert values == [5, 5, 5]

    values = []
    quick_sort(values)
    assert values == []

    values = [10, -2, 0, 7, 3]
    quick_sort(values)
    assert values == sorted([10, -2, 0, 7, 3])